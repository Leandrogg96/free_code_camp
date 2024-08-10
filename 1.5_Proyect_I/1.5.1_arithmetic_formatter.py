def arithmetic_arranger(problems, show_answers=False):
     # Error: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    results = []

    for problem in problems:
        parts = problem.split()
        first_operand, operator, second_operand = parts

        # Error: Invalid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Error: Non-digit characters
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Error: Operand too long
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the result if show_answers is True
        if operator == '+':
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))

        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)
        results.append(result)

    # Formatting
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line.append(first_operands[i].rjust(width))
        second_line.append(operators[i] + ' ' + second_operands[i].rjust(width - 2))
        dashes_line.append('-' * width)
        answers_line.append(results[i].rjust(width))

    # Combine the lines with four spaces between each problem
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes_line)

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers_line)

    return arranged_problems
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')