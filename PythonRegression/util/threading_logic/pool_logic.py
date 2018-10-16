from multiprocessing.dummy import Pool
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_pool(function,iterations,args):
    iteration_list = [int(iterations)]
    pool = Pool(processes=4)
    list_of_threads = {pool.apply_async(function,args): iteration for iteration in iteration_list}
    logger.info(list_of_threads)
    return list_of_threads


def fetch_results(id, timeout):
    try:
        response = id.get(timeout)
        logger.info(response)
        return response
    except Exception as e:
        logger.info(e)
