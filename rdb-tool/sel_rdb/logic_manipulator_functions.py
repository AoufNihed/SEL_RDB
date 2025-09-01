#!/usr/bin/env python3

import re

# Fix the relative imports
try:
    from . import helpers
    from . import sel_logic_count
except (ImportError, ValueError):
    import helpers
    import sel_logic_count


def getInstVals(name):
    """ For an instantiated variable type, get the usage
    so PLT13 returns PLT13S and PLT13R
    """
    # This is a placeholder implementation
    return []

def getSimpleAlias(name):
    """ Get the simple alias for a variable
    """
    # This is a placeholder implementation
    return name

def countLinesUsed(text):
    """ Count the lines used in the text
    """
    # This is a placeholder implementation
    return len(text.split('\n'))

def getCommentedLines(text):
    """ Get commented lines from the text
    """
    # This is a placeholder implementation
    lines = text.split('\n')
    commented_lines = [line for line in lines if line.strip().startswith(';')]
    return commented_lines

def getNonCommentedLines(text):
    """ Get non-commented lines from the text
    """
    # This is a placeholder implementation
    lines = text.split('\n')
    non_commented_lines = [line for line in lines if not line.strip().startswith(';')]
    return non_commented_lines

def getLogicLines(text):
    """ Get logic lines from the text
    """
    # This is a placeholder implementation
    lines = text.split('\n')
    logic_lines = [line for line in lines if 'SV' in line and '=' in line]
    return logic_lines

def getLogicElements(text):
    """ Get logic elements from the text
    """
    # This is a placeholder implementation
    elements = []
    # Find all logic elements using regex
    pattern = r'[A-Z]{2,}[0-9]+'
    matches = re.findall(pattern, text)
    elements.extend(matches)
    return list(set(elements))

def getLogicVariables(text):
    """ Get logic variables from the text
    """
    # This is a placeholder implementation
    variables = []
    # Find all logic variables using regex
    pattern = r'[A-Z][A-Z0-9]+'
    matches = re.findall(pattern, text)
    variables.extend(matches)
    return list(set(variables))

def getLogicFunctions(text):
    """ Get logic functions from the text
    """
    # This is a placeholder implementation
    functions = []
    # Find all logic functions using regex
    pattern = r'[A-Z]{2,}[0-9]*\('
    matches = re.findall(pattern, text)
    functions.extend([match.rstrip('(') for match in matches])
    return list(set(functions))

def getLogicOperators(text):
    """ Get logic operators from the text
    """
    # This is a placeholder implementation
    operators = []
    # Find all logic operators
    operator_list = ['AND', 'OR', 'NOT', 'XOR', 'NAND', 'NOR']
    for op in operator_list:
        if op in text:
            operators.append(op)
    return list(set(operators))

def getLogicConstants(text):
    """ Get logic constants from the text
    """
    # This is a placeholder implementation
    constants = []
    # Find all logic constants using regex
    pattern = r'\"[A-Z0-9_]+\"'
    matches = re.findall(pattern, text)
    constants.extend([match.strip('"') for match in matches])
    return list(set(constants))

def getLogicTimers(text):
    """ Get logic timers from the text
    """
    # This is a placeholder implementation
    timers = []
    # Find all logic timers using regex
    pattern = r'T[MR][0-9]+'
    matches = re.findall(pattern, text)
    timers.extend(matches)
    return list(set(timers))

def getLogicCounters(text):
    """ Get logic counters from the text
    """
    # This is a placeholder implementation
    counters = []
    # Find all logic counters using regex
    pattern = r'C[MR][0-9]+'
    matches = re.findall(pattern, text)
    counters.extend(matches)
    return list(set(counters))

def getLogicRegisters(text):
    """ Get logic registers from the text
    """
    # This is a placeholder implementation
    registers = []
    # Find all logic registers using regex
    pattern = r'R[0-9]+'
    matches = re.findall(pattern, text)
    registers.extend(matches)
    return list(set(registers))

def getLogicLatches(text):
    """ Get logic latches from the text
    """
    # This is a placeholder implementation
    latches = []
    # Find all logic latches using regex
    pattern = r'L[0-9]+'
    matches = re.findall(pattern, text)
    latches.extend(matches)
    return list(set(latches))

def getLogicSequencers(text):
    """ Get logic sequencers from the text
    """
    # This is a placeholder implementation
    sequencers = []
    # Find all logic sequencers using regex
    pattern = r'S[QV][0-9]+'
    matches = re.findall(pattern, text)
    sequencers.extend(matches)
    return list(set(sequencers))

def getLogicMathFunctions(text):
    """ Get logic math functions from the text
    """
    # This is a placeholder implementation
    math_functions = []
    # Find all logic math functions
    math_list = ['ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'ABS', 'MAX', 'MIN']
    for func in math_list:
        if func in text:
            math_functions.append(func)
    return list(set(math_functions))

def getLogicComparisonOperators(text):
    """ Get logic comparison operators from the text
    """
    # This is a placeholder implementation
    comparison_operators = []
    # Find all logic comparison operators
    comparison_list = ['EQ', 'NE', 'GT', 'GE', 'LT', 'LE']
    for op in comparison_list:
        if op in text:
            comparison_operators.append(op)
    return list(set(comparison_operators))

def getLogicBitwiseOperators(text):
    """ Get logic bitwise operators from the text
    """
    # This is a placeholder implementation
    bitwise_operators = []
    # Find all logic bitwise operators
    bitwise_list = ['AND', 'OR', 'XOR', 'NOT', 'SHL', 'SHR']
    for op in bitwise_list:
        if op in text:
            bitwise_operators.append(op)
    return list(set(bitwise_operators))

def getLogicSpecialFunctions(text):
    """ Get logic special functions from the text
    """
    # This is a placeholder implementation
    special_functions = []
    # Find all logic special functions
    special_list = ['MUX', 'DEMUX', 'ENC', 'DEC', 'CMP', 'ALU']
    for func in special_list:
        if func in text:
            special_functions.append(func)
    return list(set(special_functions))