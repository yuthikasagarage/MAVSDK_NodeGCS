import asyncio
from mavsdk import System
from flask import Blueprint, jsonify
from flask import Flask

async def run():

        drone = System()
        await drone.connect(system_address="udp://:14540")

        print("Waiting for drone to connect...")
        async for state in drone.core.connection_state():
            if state.is_connected:
                print(f"Drone discovered with UUID: {state.uuid}")
                break

        print("Waiting for drone to have a global position estimate...")
        async for health in drone.telemetry.health():
            if health.is_global_position_ok:
                print("Global position estimate ok")
                break

        print("-- Arming")
        await drone.action.arm()

        print("-- Taking off")
        await drone.action.takeoff()

        await asyncio.sleep(5)

        print("-- Landing")
        await drone.action.land()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
main = Flask(__name__)

@main.route('/take_off')
def takeoff(): 

    if __name__ == "__main__":
        main.run(debug=False, use_reloader=False)
        return loop.run_until_complete(run())

       
