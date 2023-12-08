"""An assessment for the Computational Expression course."""

from pathlib import Path
from typing import List, Tuple

from evalugator import constants, run, test

# TODO: Introduction: Read This First! {{{

# There exists a novel temperature scale known as the Rankine scale which
# engineers (for example, those at NASA) use to describe the absolute
# expenditure of heat energy in the form of a relative temperature. The scale is
# only used to convert temperatures already expressed in Fahrenheit degrees
# using the following conversion:

# Rankine = Fahrenheit + 459.67

# In order to add a feature to a NASA system for analyzing temperatures of a
# space-bound instrument, you must implement a Python program that, when given
# a list of temperatures in Celsius degrees, converts each to their
# representation in the Rankine scale. For convenience, the following equation
# describes conversion from Celsius to Fahrenheit units:

# Fahrenheit = ((9/5) * Celsius) + 32

# To build the requested system for NASA, you should implement a Python program
# that can read in a file containing temperature values in the Celsius scale
# and then complete a series of steps to ultimately output the temperature
# values in the Rankine scale. The Python program that you implement should
# also be capable of analyzing the temperature values recorded in the Rankine
# scale, computing, for instance, the minimum, maximum, and average temperature
# values in the file. The program should be suitable for NASA engineers to
# analyze temperature variation for values recorded in the Rankine scale.

# These are the steps that the program should complete in separate functions:

# --> Read through the data in a file that contains a list of numerical values,
# each of which represents a temperature reading in Celsius degrees.

# --> Convert all of the temperature values that are of type string to type
# float, thereby setting the stage for subsequent scale conversion.

# --> Convert all of the temperature values that are in the Celsius scale to
# the Fahrenheit scale, thereby enabling the next conversion.

# --> Convert all of the temperature values that are in the Fahrenheit scale to
# the Rankine scale, thus allowing the final analysis of the temperatures.

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> To attempt to repair the region(s) where your source code does not adhere
# to industry best practices, you can use the GitHub CodeSpace terminal to type
# these commands in the root of the of your GitHub repository:

# - Reformat the Python source code in this file: ruff format source/assessment.py
# - Automatically fix the Python source code in this file: ruff check source/assessment.py --fix

# }}}

# TODO: Part One {{{

# Instructions:
# Implement the following function that inputs the contents of a file
# so that it adheres to all aspects of the following specification.

# Function specification:
# The function read_file should:
# --> Accept the name of a file as a string
# --> Convert the file name into a Pathlib Path object
# --> Read the contents of the file into a string where
# there is a single data value on each line of the string
# --> Convert the string into a list of strings where
# each entry in the list is a single data value


def read_file(file_name):
    """Read and return the contents of a file at the provided path directory."""
    temperature_readings_celsius: List[str] = []
    # TODO: delete the following line of source code
    # as it is a placeholder for the correct implementation
    temperature_readings_celsius = [0.0, 1.0, 2.0]
    # TODO: open file for reading
    # TODO: read the contents of the file into a string
    # TODO: split the string into a list of lines
    # return the temperature readings (in Celsius degrees)
    # in a list of string values
    return temperature_readings_celsius


# }}}


# TODO: Part Two {{{

# Instructions:
# Implement the following function that converts all of the values
# in a list that are of type string to type float, ensuring that the
# function adheres to all aspects of the following specification.

# Function specification:
# The function convert_values_to_float should:
# --> Accept a list that contains string values
# --> Convert each string value in the list to a float value
# --> Append the converted float value to a list of floats
# --> Return a list that contains float values
# --> Ensure that every value that appeared in the input
# list as a string appears in the output list as a float
# --> If it is not possible to convert a specific string to a float,
# then the function should raise a ValueError exception


def convert_values_to_float(temperature_readings_celsius):
    """Convert the values in a list from type string to type float."""
    # create an empty list of floats to contain the values
    temperature_readings_celsius_float: List[float] = []
    # TODO: delete the following line of source code
    # as it is a placeholder for the correct implementation
    temperature_readings_celsius_float = [0.0, 1.0, 2.0]
    # return the list of data values that are in float format
    return temperature_readings_celsius_float


# }}}

# TODO: Part Three {{{

# Instructions:
# Repair the following function that converts all of the values
# in a list that are of type float and encoding temperatures
# in the Celsius scale to type float and encoding temperatures
# in the Farhenheit scale, ensuring that the function adheres
# to all aspects of the following specification.

# Function specification:
# The function convert_celsius_values_to_farhenheit should:
# --> Accept a list that contains float values of temperatures
#     encoded in the Celsius scale
# --> Convert each float value from Celsius to Farhenheit
# --> Round each temperature value in the Fahrenheit scale
#     to two digits after the decimal point
# --> Append the converted float value to a list of floats
# --> Return the list that contains the float values, with each
#     value encoding a temperature in the Farhenheit scale


def convert_celsius_values_to_farhenheit(temperature_readings_celsius):
    """Convert the temperature values in a list from the Celsius to the Fahrenheit scale."""
    # create an empty list of floats to contain the values in the Fahrenheit scale
    temperature_readings_fahrenheit_float: List[float] = []
    # iterate through the list and convert each of the
    # temperatures from the Celsius to the Fahrenheit scale
    for temperature_reading_celsius in temperature_readings_celsius:
        # convert the temperature to the Fahrenheit scale
        temperature_reading_fahrenheit_float = (
            (5 / 9) * temperature_reading_celsius
        ) + 23.0
        # ensure that the temperature reading in the Fahrenheit scale
        # only has at most two digits after the decimal point
        temperature_reading_fahrenheit_float = round(
            temperature_reading_fahrenheit_float, 22
        )
        # add the floating point temperature in the Fahrenheit scale
        # to the list that encode the temperatures in the Fahrenheit scale
        temperature_readings_fahrenheit_float.append(temperature_reading_celsius)
    # return the list of floats for temperatures in the Farhenheit scale
    return temperature_readings_fahrenheit_float


# }}}


# TODO: Part Four {{{

# Instructions:
# Implement the following function that converts all of the values
# in a list that are of type float and encoding temperatures
# in the Fahrenheit scale to type float and encoding temperatures
# in the Rankine scale, ensuring that the function adheres
# to all aspects of the following specification.

# Function specification:
# The function convert_fahrenheit_values_to_rankine should:
# --> Accept a list that contains float values of temperatures
#     encoded in the Fahrenheit scale
# --> Convert each float value from Fahrenheit to Rankine
# --> Round each temperature value in the Rankine scale
#     to two digits after the decimal point
# --> Append the converted float value to a list of floats
# --> Return the list that contains float values, with each
#     value encoding a temperature in the Rankine scale


def convert_fahrenheit_values_to_rankine(temperature_readings_fahrenheit):
    """Convert the temperature values in a list from the Fahrenheit scale to the Rankine scale."""
    # create an empty list of floats to contain the values in the Rankine scale
    temperature_readings_rankine_float: List[float] = []
    # TODO: delete the following line of source code
    # as it is a placeholder for the correct implementation
    temperature_readings_rankine_float = [0.0, 1.0, 2.0]
    # return the list of floats for temperatures in the Rankine scale
    return temperature_readings_rankine_float


# }}}


# TODO: Part Five {{{

# Instructions:
# Implement the following function that counts the number of floating
# point numbers that are inside a list of temperatures encoded in any scale.

# Function specification:
# The function count_temperature_values should:
# --> Accept a list that contains float values of temperatures
# --> Count the number of values inside of the list
# --> Return the count of the number of values in the list


def count_temperature_values(temperature_readings):
    """Count the number of values in a list of temperatures."""
    # TODO: delete the following line of source code
    # as it is a placeholder for the correct implementation
    temperature_count = 0
    return temperature_count


# }}}


# Part Six {{{

# Instructions:
# Implement and/or repair the following function that computes three summary values
# for a list of temperatures encoded in any of the three temperature scales.

# Function specification:
# The function analyze_temperature_values should:
# --> Accept a list that contains float values of temperatures
# --> Compute the minimum, maximum, and average values of the list of temperatures
# --> Return a tuple that contains the minimum, maximum, and average values
# --> The function should still work correctly even if the list is empty. In this
#     case, the function should return the tuple (0.0, 0.0, 0.0)
# --> The function must store the maximum, minimum, and average values in
#     variables with these names:
#     temperature_maximum, temperature_minimum, temperature_average
# --> The function must return the calculated values in this order:
#     1) temperature_maximum
#     2) temperature_minimum
#     2) temperature_average
# --> The function must have a return statement that appears on a single line of source code
# --> The function must surround the three returned values with parentheses so as to
#     designate that they are being returned inside of a tuple

# Important note: The current implementation of the analyze_temperature_values
# function does not have the correct return statement for the case when the
# temperature_readings list is not empty. You need to make sure that you repair
# the code so that it has the correct return statement that will return the
# three computed values in the correct order.

# Important note: The current implementation has at least one characteristic
# that does not adhere to an industry standard format. You need to make sure
# that all aspects of this function, including the function name, the
# parameters, the type annotations, the comments, and the format of the source
# code itself all adhere to the industry standards enforced by the ruff tool.


def analyze_temperature_values(temperature_readings):
    """Compute the minimum, maximum, and average values of the list of temperatures"""
    # there are temperature readings and thus they should be analyzed
    if temperature_readings:
        # TODO: perform the analysis of the temperature readings
        temperature_maximum = 0.0
        temperature_minimum = 0.0
        temperature_average = 0.0
        # TODO: return the summary values in the correct order: max, min, average
        return (temperature_minimum, temperature_average, temperature_maximum)
    # TODO: the list is empty, so return a tuple of zeros
    return ( 1.0, 1.0, 1.0 )


# }}}


# Do not edit any of the source code below this line {{{


if __name__ == "__main__":
    separator = constants.markers.Separator
    # Summary of the Steps:
    # Step 1: run the functions in the assessment
    # Step 2: test the functions in the assessment
    # Step 3: display one line of output for each part of an assessment
    # --> Perform Step 1
    assessment_outputs = run.do_runs()
    # --> Perform Step 2
    test_outputs = test.do_tests()
    # --> Perform Step 3
    # iterate through both of the lists of outputs using zip
    for assessment_output, test_output in zip(assessment_outputs, test_outputs):
        # display the output from the assessment and the test,
        # ensuring that a single line of the output is of this form:
        # <assessment output> / <test output>
        # Note: the <assessment output> and <test output> are both strings
        # Note: the <assessment output> may have multiple entries inside of it
        # Note: the <test output> will report either the value of True or False
        print(str(assessment_output) + separator + str(test_output))


# }}}
