from multiprocessing.dummy import Pool
import multiprocessing as mp
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def start_pool(function,iterations,args):
    #Assigns the process worker pool to either the cpu count or the number of nodes for the call, whichever is lower
    pool = Pool(processes=len(args) if len(args) <= mp.cpu_count() else mp.cpu_count())
    future_results = []
    iteration = 0
    while iteration < int(iterations):
        run_list = (node for node in args if iteration < int(iterations))
        for node in run_list:
            iteration += 1
            arg_list = (node,args[node])
            future_results.append(pool.apply_async(function,arg_list))
    return future_results


def fetch_results(future_result, timeout):
    try:
        response = future_result.get(timeout)
        logger.debug(response)
        return response
    except Exception as e:
        logger.debug(e)
