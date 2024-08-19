import pytest
from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    spark_session = get_spark_session("LOCAL")
    return spark_session

@pytest.fixture
def expected_results(spark):
    "gives the expected results"
    results_schema = "state string,count int"
    return spark.read.format("csv").schema(results_schema).load("data/test_result/state_aggregate.csv")