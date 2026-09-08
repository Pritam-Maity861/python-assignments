'''
Now create an async job runner func run_jobs . The following conditions must be met.
1. All 20 jobs must eventually be processed.
2. A maximum of 3 jobs may run simultaneously.
3. Collect and return the results of all completed jobs.
4. Print the total execution time
'''

import asyncio
import random
import time

job_semaphore = asyncio.Semaphore(3)

async def process_job(job_id):
    async with job_semaphore:
        print(f"Job {job_id} started") 
        duration = random.uniform(1, 3)
        await asyncio.sleep(duration)  
        print(f"Job {job_id} completed (took {duration:.2f}s)")
        
        return job_id

async def run_jobs(jobs_list):
    start_time = time.perf_counter()
    tasks = [asyncio.create_task(process_job(job)) for job in jobs_list]
    results = await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    print(f"\nAll jobs processed! Total execution time: {end_time - start_time:.2f} seconds")
    
    return results

if __name__ == "__main__":
    jobs = list(range(1, 21))
    final_results = asyncio.run(run_jobs(jobs))
    print(f"Returned IDs list: {final_results}")
