import json
from phi.model.openai import OpenAIChat
from phi.agent.duckdb import DuckDbAgent



data_analyst = DuckDbAgent(
    model=OpenAIChat(model="gpt-4o"),
    semantic_model=json.dumps(
        {
            "tables": [
                 {
                    "name": "ferry-trips-data",
                    "description": (
                        "A CSV file containing records of trips made by 5 ferries owned by Färjerederiet. "
                        "Contains data from 5 ferries owned and operated by Färjerederiet:\n\n"
                        "- Fragancia\n"
                        "- Jupiter\n"
                        "- Merkurius\n"
                        "- Nina\n"
                        "- Yxlan\n\n"
                        "The data corresponds to the time period between 2023-03-01 and 2024-02-29. "
                        "PONTOS-HUB launched on 2023-04-30, so the data contains datapoints corresponding to a period for "
                        "which PONTOS-HUB has no data.\n\n"
                        "Each row in the `ferry_trips_data.csv` files contain fields describing 2 trips between two terminals:\n\n"
                        "- An `outbound` trip from the departure terminal to the arrival terminal.\n"
                        "- An `inbound` trip from the arrival terminal to the departure terminal.\n\n"
                        "The suffixes `outbound` and `inbound` in the field names indicate to which trip does the field correspond.\n\n"
                        "Here follows a description of _some_ of the fields as most of them are self-explanatory:\n\n"
                        "Original fields:\n\n"
                        "- `time_departure`: Time of departure for the outbound trip as recorded by Färjerederiet. Given in Central European Time (CET).\n"
                        "- `vehicles_left_at_terminal_outbound/inbound`: Number of vehicles left at the terminal on departure for the outbound/inbound trip. _Estimated by the crew._\n"
                        "- `trip_type`: One of the following types of trip:\n"
                        "  - `ordinary`- Ordinary trip.\n"
                        "  - `doubtful` – An \"ordinary\" trip that does not match the timetable.\n"
                        "  - `extra` – An extra trip by an additional ferry that does not follow the timetable.\n"
                        "  - `proactive` – A trip made before the ordinary trip to stay ahead, comparable to an extra trip.\n"
                        "  - `doubling` – An extra trip between two regular trips to take care of vehicles left behind in the terminal.\n"
                        "- `tailored_trip`: A special trip for vehicles with dangerous cargo. (1: True, 0: False).\n"
                        "- `passenger_car_equivalent_outbound/inbound`: The total number of vehicles in a outbound/inbound trip as Passenger Car Equivalent (PCE) according to the following conversion rules:\n"
                        "  - Length 0-6 meters (e.g., car): 1 PCE\n"
                        "  - Length 6-12 meters (e.g., lorry or car with trailer): 2.5 PCE\n"
                        "  - Length 15-24 meters (e.g., lorry with trailer): 4.5 PCE\n"
                        "  - Bus: 9 PCE\n"
                        "  - Other large vehicles (e.g., cranes, harvesters): 9 PCE\n\n"
                        "Additional fields calculated with data from PONTOS-HUB (might not always contain values depending on data availability):\n\n"
                        "- `distance_outbound/inbound_nm`: Approximate distance travelled in the outbound/inbound trip. Calculated from PONTOS-HUB data and given in nautical miles.\n"
                        "- `fuelcons_outbound/inbound_l`: Approximate fuel consumption in the outbound/inbound trip. Calculated from PONTOS-HUB data and given in liters.\n"
                        "- `start_time_outbound/inbound`: Approximate start time of the outbound/inbound trip. Calculated from PONTOS-HUB data and given in CET.\n"
                        "- `end_time_outbound/inbound`: Approximate end time of the outbound/inbound trip. Calculated from PONTOS-HUB data and given in CET."
                    ),
                    "path": "ferry_trips_data.csv",
        },
        {   
            "name": "ferries-info",
            "description": "A JSON file containing information of the ferries owned by Färjerederiet that share their data to PONTOS-HUB. The `pontos_vessel_id` key-value pair can be use for querying the REST-API of PONTOS-HUB.",
            "path": "ferries.json"
        },
        {   
            "name": "ljusteroleden_oktober_april_schedule",
            "description": " Schedules for the ferry route Ljusteroleden",
            "path": "schedules/ljusteroleden_oktober_april_utg22_2020_w.csv"
        },
        {   
            "name": "furusundsleden-blidoleden-schedule",
            "description": " Schedules for the ferry route Furusundsleden, Yxlan ferry",
            "path": "schedules/furusundsleden-blidoleden_utg9_200623_w.csv"
        }
            ]
        }
    ),
    markdown=True,
)

"""
data_analyst.print_response(
    "Show me a histogram of passenger_car_equivalent_outbound + passenger_car_equivalent_inbound for route called Ljusteröleden"
    "Choose an appropriate bucket size but share how you chose it. "
    "Show me the result as a pretty ascii diagram",
    stream=True,
)
"""
"""
data_analyst.print_response(
    "Perform a cost-benefit analysis for maintaining current trip frequencies versus potential savings from reduced fuel consumption during low demand. Columns fuelcons_outbound/inbound_l contains fuel consumption value. passenger_car_equivalent_outbound/inbound is how busy the trip was. \
     By looking in the schedule table for this route, suggest which adjustment to the timetable should be made based on the demand patterns, propose a more efficient schedule for the Ljusteröleden route to minimize fuel consumption while maintaining service quality. \
    Provide recommendations for adjusting the number of trips during low-demand periods to save fuel. \
    Estimate potential cost savings over a year if low-demand trips are reduced by 20%.",
    stream=True,
)
"""

print("Type 'exit' to quit.")
while True:
    user_input = input("Ask your question: ")
    if user_input.lower() == 'exit':
        break
    data_analyst.print_response(user_input, stream=True)