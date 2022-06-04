
import pytest
from fastapi.testclient import TestClient


TEST_PROGRAMS = [
    "1000 meter swim",
    "5 km run",
    "20 mile bike",
    "20 min swim\n20 min bike",
    "4 rounds:\n400 meter run\n75 meter swim\n1 min rest ;",
    "AMRAP 18 min:\n600 meter run\n100 meter swim ;",
    "2 km row\n1 mile run\n2 km row",
    "400 meter run\n90 sec rest\n200 meter run\n60 sec rest\n100 meter run",
    "AMRAP 20 min:\n5 handstand_pushup\n10 pistol\n15 pullup ;",
    "AMRAP 20 min:\n5 pullup\n10 pushup\n15 squat ;",
    "5 rounds:\n400 meter run\n15 95 lb barbell overhead_squat ;",
    "3 rounds:\n50 squat\n7 muscle_up\n10 135 lb barbell hang_clean ;",
]


def test_get(api_client: TestClient):
    """
    GET /
    """
    api_client.get("/")


@pytest.mark.parametrize("program_str", TEST_PROGRAMS)
def test_parse(program_str, api_client: TestClient):
    """
    POST /parse
    """
    res = api_client.post(
    	"/parse", 
    	json = {'message': program_str}
    )
    print('\n' + str(res.json()))



@pytest.mark.parametrize("program_str", TEST_PROGRAMS)
def test_timers(program_str, api_client: TestClient):
    """
    POST /timers
    """
    res = api_client.post(
    	"/timers", 
    	json = {'message': program_str}
    )
    print('\n' + str(res.json()))
