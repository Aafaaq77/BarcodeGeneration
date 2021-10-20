from print_jobs import PrintJob
from users import User
import barcode # or blabel TODO
# import win32, win32print, win32api


def get_codes_from_job(print_job: PrintJob, code_type):
    '''
    TODO Change function. Accept everything required and then create the job.
    '''
    return generate_barcodes(
        job_code=print_job.job_code, start=print_job.start+1,
        end_code=print_job.last_code, code_type=code_type
    )

def generate_barcodes(job_code: str, start: int, end_code: str, total_codes: int=1000, code_type='code39'):
    '''
    Generates given number of codes. Default: 1000 code39 codes
    returns a generator object with all the barcode objects.
    '''
    CODE = barcode.get_barcode_class(code_type)

    return (
        CODE(f'{job_code} {str(code).zfill(7)} {end_code}')
        for code in range(start, start+total_codes)
    )


if __name__ == '__main__':
    codes = get_codes_from_job(PrintJob('ABC', 1, 1000, 'E', User('muster335', password='my_defaut_pass')))
    for _ in range(10):
        print(next(codes))