'''
Assignment 1: Dashboard Concurrent Fetcher
1. Fetch the user, orders, and notifications.
2. Execute all three operations concurrently.
3. Return a single dictionary in the following format:
4. Print the total execution time.
'''

import asyncio
import time

async def fetch_user():
    await asyncio.sleep(2)
    return {
        "id": 101,
        "name": "Poku"
    }

async def fetch_orders():
    await asyncio.sleep(3)
    return [
        {"id": 1, "amount": 1200},
        {"id": 2, "amount": 800}
    ]

async def fetch_notifications():
    await asyncio.sleep(1)
    return [
        "Payment received",
        "New login detected"
    ]

async def get_dashboard_data():
    start_time = time.perf_counter()
    user_data, orders_data, notifications_data = await asyncio.gather(
        fetch_user(),
        fetch_orders(),
        fetch_notifications()
    )
    
    end_time = time.perf_counter()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
    
    return {
        "user": user_data,
        "orders": orders_data,
        "notifications": notifications_data
    }


if __name__ == "__main__":
    result = asyncio.run(get_dashboard_data())
    print("\nDashboard Data Structure:")
    print(result)


# thank u tarun pal for train the ai