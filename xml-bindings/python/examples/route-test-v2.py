# Bindings generated from S-421 2.0.0 Beta schema 
# The data is partially based on an RTZ file originally shared in Baltic 
# Sea activities, vessel identifying information has been randomized.

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from s421 import *

envelope=Envelope()
envelope.lower_corner = [0.0, 0.0]
envelope.upper_corner = [90.0, 90.0]

dataset = Dataset(
    bounded_by=BoundedBy(
        envelope=envelope
    ),
    route = Route(
        id = "RTE",
        route_id = "urn:mrn:foobar:random:route",
        route_edition_no = 4,
        route_info=RouteInfo(
            id = "RTE.INFO",
            route_info_status = 4,
            route_info_vessel_mmsi = "313313313",
            route_info_vessel_imo = "3133313",
            route_info_vessel_voyage = "urn:mrn:foobar:313313313:random:voyage",
            route_info_name = "Pakri Anchorage D - Paldiski Lounasadam N6",
            route_info_vessel_name = "Duckville Star",
        ),
        route_waypoints = RouteWaypoints(
            bounded_by=BoundedBy(
                envelope=envelope
            ),
            route_waypoint = [
                RouteWaypoint(
                    id = "RTE.WPT.8",
                    route_waypoint_turn_radius = "0.0",
                    geometry = GmPoint(
                        point = Point1(
                            id = "RTE.WPT.8.PT",
                            pos = "59.36948333 23.89871667"
                        )
                    ),
                    route_waypoint_name = "Pakri D Anchorage",
                    route_schedule_element = RouteScheduleElement(
                        id = "RTE.SCHED.1.MAN.ELEMENT.8",
                        route_schedule_element_type = "manual",
                        route_schedule_element_etd = "2100-01-01T12:00:15Z"
                    )
                ),
                RouteWaypoint(
                    id = "RTE.WPT.7",
                    route_waypoint_turn_radius = "1.0",
                    geometry = GmPoint(
                        point = Point1(
                            id = "RTE.WPT.7.PT",
                            pos = "59.34137194 24.03977042"
                        )
                    ),
                    route_waypoint_name = "turn to Achrage D"
                ),
                RouteWaypoint(
                    id = "RTE.WPT.10",
                    route_waypoint_turn_radius = "1.0",
                    geometry = GmPoint(
                        point = Point1(
                            id = "RTE.WPT.10.PT",
                            pos = "59.37216577 23.98967083"
                        )
                    ),
                    route_waypoint_name = "turn to Achrage D"
                ),
                RouteWaypoint(
                    id = "RTE.WPT.5",
                    route_waypoint_turn_radius = "0.3",
                    geometry = GmPoint(
                        point = Point1(
                            id = "RTE.WPT.5.PT",
                            pos = "59.32638127 24.05757044"
                        )
                    ),
                    route_waypoint_name = "Fairway",
                    route_schedule_element = RouteScheduleElement(
                        id = "RTE.SCHED.1.MAN.ELEMENT.5",
                        route_schedule_element_type = "calculated",
                        route_schedule_element_etd = "2100-01-01T12:15:00Z",
                        route_schedule_element_plan_sog = 5.3
                    ),
                    route_waypoint_leg = RouteWaypointLeg(
                        id = "RTE.WPT.5.LEG",
                        route_waypoint_leg_dynamic_ukc = 7.5,
                        route_waypoint_leg_geometry_type = 1
                    )
                ),
                RouteWaypoint(
                    id = "RTE.WPT.9",
                    route_waypoint_turn_radius = "0.5",
                    geometry = GmPoint(
                        point = Point1(
                            id = "RTE.WPT.9.PT",
                            pos = "59.32905343 24.0771707"
                        )
                    ),
                    route_waypoint_leg = RouteWaypointLeg(
                        id = "RTE.WPT.9.LEG",
                        route_waypoint_leg_dynamic_ukc = 7.5,
                        route_waypoint_leg_geometry_type = 1
                    )
                ),
                RouteWaypoint(
                    id = "RTE.WPT.3",
                    route_waypoint_turn_radius = "0.0",
                    geometry = GmPoint(
                        point = Point1(
                            id = "RTE.WPT.3.PT",
                            pos = "59.33208224 24.08424672"
                        )
                    ),
                    route_waypoint_name = "Paldiski Berth nr 8",
                    route_schedule_element = RouteScheduleElement(
                        id = "RTE.SCHED.1.MAN.ELEMENT.3",
                        route_schedule_element_type = "manual",
                        route_schedule_element_etd = "2100-01-01T13:00:00Z"
                    ),
                    route_waypoint_leg = RouteWaypointLeg(
                        id = "RTE.WPT.3.LEG",
                        route_waypoint_leg_dynamic_ukc = 2.2,
                        route_waypoint_leg_geometry_type = 1
                    )
                )
            ]
        )
    )
)

serializer = XmlSerializer()
serializer.config.indent = "  "
print(serializer.render(dataset))
