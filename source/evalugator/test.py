"""Test the functions that are a part of an assessment."""

# ruff: noqa: PLR2004

from typing import Any, List

import assessment
from evalugator import constants, execute

FILE_NAME = constants.files.Temperature_File_Name


def do_tests() -> List[Any]:
    """Test all of the sub-parts of the assessment."""
    # execute all of the test cases defined in this module
    # and then return their output in a list of strings,
    # with each entry in the list the output of one test
    test_output: List[str] = []
    test_output = execute.execute_by_name_filter(
        constants.evalugator.Test_Module, constants.evalugator.Test_Filter
    )
    return test_output


def test_part_one():
    """Test the function defined by part-one of the assessment."""
    # call the function under test
    part_one_output = assessment.read_file(FILE_NAME)
    # calculate the number of rows in the output
    row_count = len(part_one_output)
    try:
        # check: the number of rows in the output should be 100
        assert row_count == 10
        # check: the output should be a list containing strings
        assert isinstance(part_one_output, list) is True
        # check: each entry in the output should be a string
        assert all(isinstance(entry, str) for entry in part_one_output)
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_two():
    """Test the function defined by part-two of the assessment."""
    # call the function under test
    part_two_output = assessment.read_file(FILE_NAME)
    # calculate the number of rows in the output
    row_count = len(part_two_output)
    try:
        # check: the number of rows in the output should be 100
        assert row_count == 10
        # check: the output should be a list containing strings
        assert isinstance(part_two_output, list) is True
        # check: each entry in the output should be a string
        assert all(isinstance(entry, str) for entry in part_two_output)
        # convert the list of strings to a list of floats
        part_two_output = assessment.convert_values_to_float(part_two_output)
        # check: the output should be a list
        assert isinstance(part_two_output, list) is True
        # check: each entry in the output should be a float
        assert all(isinstance(entry, float) for entry in part_two_output)
        # check: confirm that the correct value is in the first index
        assert part_two_output[0] == 34.64
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_three():
    """Test the function defined by part-three of the assessment."""
    part_three_input = [0.0, 10.0, 20.0]
    # call the function under test
    part_three_output = assessment.convert_celsius_values_to_farhenheit(part_three_input)
    try:
        # check: the output should be a list
        assert isinstance(part_three_output, list) is True
        # check: each entry in the output should be a float
        assert all(isinstance(entry, float) for entry in part_three_output)
        # check: the output should contain three entries
        assert len(part_three_output) == 3
        # check: the output should contain the correct values
        assert part_three_output == [32.0, 50.0, 68.0]
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_four():
    """Test the function defined by part-four of the assessment."""
    part_four_input = [0.0, 10.0, 20.0]
    # call the function under test
    part_four_output = assessment.convert_celsius_values_to_farhenheit(part_four_input)
    # call the final function under test
    part_four_output_final = assessment.convert_fahrenheit_values_to_rankine(part_four_output)
    try:
        # check: the output should be a list
        assert isinstance(part_four_output_final, list) is True
        # check: each entry in the output should be a float
        assert all(isinstance(entry, float) for entry in part_four_output_final)
        # check: the output should contain three entries
        assert len(part_four_output_final) == 3
        # check: the output should contain the correct values
        assert part_four_output_final == [491.67, 509.67, 527.67]
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_five():
    """Test the function defined by part-five of the assessment."""
    # create a list as input with multiple floating point values
    part_five_input = [0.0, 10.0, 20.0, 30.0]
    # call the function under test
    part_five_output = assessment.count_temperature_values(part_five_input)
    try:
        # check: the output should be an integer
        assert isinstance(part_five_output, int) is True
        # check: the output should be 4
        assert part_five_output == 4
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False


def test_part_six():
    """Test the function defined by part-six of the assessment."""
    # run the function under test with different inputs
    # initial list of temperatures
    temperatures_first = [0.0]
    value_analysis_first = assessment.analyze_temperature_values(temperatures_first)
    # empty list of temperatures
    temperatures_empty = []
    value_analysis_empty = assessment.analyze_temperature_values(temperatures_empty)
    # non-empty and non-zero list of temperatures
    temperatures_non_empty = [3.0, 2.0, 10.0]
    value_analysis_non_empty = assessment.analyze_temperature_values(temperatures_non_empty)
    try:
        # --> first input
        # check: the output should be a tuple of floats
        assert isinstance(value_analysis_first, tuple) is True
        # check: each of the values in the list is a float
        assert all(isinstance(entry, float) for entry in value_analysis_first)
        # check: there should be three values in the tuple
        assert len(value_analysis_first) == 3
        # check: each of the values is a zero
        assert all(entry == 0.0 for entry in value_analysis_first)
        # --> second input
        # check: the output should be a tuple of floats
        assert isinstance(value_analysis_empty, tuple) is True
        # check: each of the values in the list is a float
        assert all(isinstance(entry, float) for entry in value_analysis_empty)
        # check: there should be three values in the tuple
        assert len(value_analysis_empty) == 3
        # check: each of the values is a zero
        assert all(entry == 0.0 for entry in value_analysis_empty)
        # all of the assertions passed
        # --> third input
        # check: the output should be a tuple of floats
        assert isinstance(value_analysis_non_empty, tuple) is True
        # check: each of the values in the list is a float
        assert all(isinstance(entry, float) for entry in value_analysis_non_empty)
        # check: there should be three values in the tuple
        assert len(value_analysis_non_empty) == 3
        # check: each of the values is a not zero
        assert all(entry != 0.0 for entry in value_analysis_non_empty)
        # check: the values are correct for max, min, and average
        assert value_analysis_non_empty == (10.0, 2.0, 5.0)
        # all of the assertions passed
        return True
    except AssertionError:
        # at least one of the test case assertions failed
        return False
