"""Run the functions that are a part of an assessment."""

from typing import Any, List

import assessment
from evalugator import constants, execute

FILE_NAME = constants.files.Temperature_File_Name


def do_runs() -> List[Any]:
    """Run all of the sub-parts of the assessment."""
    # execute all of the run functions defined in this module
    # and then return their output in a list of strings,
    # with each entry in the list the output of one run
    run_output: List[str] = []
    run_output = execute.execute_by_name_filter(
        constants.evalugator.Run_Module, constants.evalugator.Run_Filter
    )
    return run_output


def run_part_one():
    """Run the function defined by part-one of the assessment."""
    separator = constants.markers.Separator
    part_one_output = assessment.read_file(FILE_NAME)
    # calculate the number of rows in the output
    row_count = len(part_one_output)
    # determine the type of the output
    output_type = type(part_one_output)
    # return the number of rows and columns inside of the list of lists
    return str(row_count) + separator + str(output_type)


def run_part_two():
    """Run the function defined by part-two of the assessment."""
    separator = constants.markers.Separator
    part_two_output = assessment.read_file(FILE_NAME)
    # calculate the number of rows in the output
    row_count = len(part_two_output)
    # determine the type of the first entry of the list;
    # run this BEFORE the conversion to a list of floats
    data_value_type_before = type(part_two_output[0])
    # convert the list of strings to a list of floats
    part_two_output_converted = assessment.convert_values_to_float(part_two_output)
    # determine the type of the first entry of the list;
    # run this AFTER the conversion to a list of floats
    data_value_type_after = type(part_two_output_converted[0])
    # return details about the list and the data type of the values in the list
    return (
        str(row_count)
        + separator
        + str(data_value_type_before)
        + separator
        + str(data_value_type_after)
    )


def run_part_three():
    """Run the function defined by part-three of the assessment."""
    separator = constants.markers.Separator
    # start with the celsius temperatures
    celsius_temperatures = [0.0, 10.0, 20.0]
    # convert these temperatures to farhenheit
    farhenheit_temperatures = assessment.convert_celsius_values_to_farhenheit(
        celsius_temperatures
    )
    # calculate the number of values in the output
    value_count = len(farhenheit_temperatures)
    # return details about the list and the values in celsius and farhenheit
    return (
        str(value_count)
        + separator
        + str(celsius_temperatures)
        + separator
        + str(farhenheit_temperatures)
    )


def run_part_four():
    """Run the function defined by part-four of the assessment."""
    separator = constants.markers.Separator
    # start with the celsius temperatures
    celsius_temperatures = [0.0, 10.0, 20.0]
    farhenheit_temperatures = assessment.convert_celsius_values_to_farhenheit(
        celsius_temperatures
    )
    # convert the farhenheit temperatures to rankine
    rankine_temperatures = assessment.convert_fahrenheit_values_to_rankine(
        farhenheit_temperatures
    )
    # calculate the number of values in the output
    value_count = len(rankine_temperatures)
    # return details about the list and the final values in all three temperature encodings
    return (
        str(value_count)
        + separator
        + str(celsius_temperatures)
        + separator
        + str(farhenheit_temperatures)
        + separator
        + str(rankine_temperatures)
    )


def run_part_five():
    """Run the function defined by part-five of the assessment."""
    separator = constants.markers.Separator
    # initial list of temperatures
    temperatures_first = [0.0]
    value_count_first = assessment.count_temperature_values(temperatures_first)
    # first list of temperatures
    temperatures_one = [0.0, 10.0, 20.0]
    value_count_one = assessment.count_temperature_values(temperatures_one)
    # second list of temperatures
    temperatures_two = [0.0, 10.0, 20.0, 30.0]
    value_count_two = assessment.count_temperature_values(temperatures_two)
    # third list of temperatures (note use of an empty list)
    temperatures_three_empty = []
    value_count_three = assessment.count_temperature_values(temperatures_three_empty)
    # return details about the list and the count of the values
    return (
        str(value_count_first)
        + separator
        + str(value_count_one)
        + separator
        + str(value_count_two)
        + separator
        + str(value_count_three)
    )


def run_part_six():
    """Run the function defined by part-six of the assessment."""
    separator = constants.markers.Separator
    # initial list of temperatures
    temperatures_first = [0.0]
    value_analysis_first = assessment.analyze_temperature_values(temperatures_first)
    # first list of temperatures
    temperatures_one = [0.0, 10.0, 20.0]
    value_analysis_one = assessment.analyze_temperature_values(temperatures_one)
    # second list of temperatures
    temperatures_two = [0.0, 10.0, 20.0, 30.0]
    value_analysis_two = assessment.analyze_temperature_values(temperatures_two)
    # third list of temperatures (note use of an empty list)
    temperatures_three_empty = []
    value_count_three = assessment.analyze_temperature_values(temperatures_three_empty)
    # return details about the list and the analysis of the data in the list
    return (
        str(value_analysis_first)
        + separator
        + str(value_analysis_one)
        + separator
        + str(value_analysis_two)
        + separator
        + str(value_count_three)
    )
