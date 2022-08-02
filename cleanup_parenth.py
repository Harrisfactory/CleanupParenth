

#a set of operators to perform general checks on
operators = {"*","/","+","-"}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Checks if inside parenthesis is a single term or polynomial
# PARAMETERS:
#   parenthesis <Tuple> indicies of paired parenthesis locations
#   expression <List> valid expression
#
# RETURNS
#   <Boolean> Is the expression not a polynomial? by checking for an operator.
#
def isSingleTerm(parenthesis, expression):
    inner_parenthesis_detected = 0
    for i in range(parenthesis[0]+1, parenthesis[1]):
        if expression[i] == '(': inner_parenthesis_detected += 1
        if not inner_parenthesis_detected:
            if expression[i] in '+-':
                return False
        if expression[i] == ')': inner_parenthesis_detected -= 1
    return True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Checks if given set of parenthesis are necessary based on adjacent left operators
# PARAMETERS:
#   parenthesis <Tuple> indicies of paired parenthesis locations
#   surrounding_operators <List> operators from the left and right of paranthesis
#
# RETURNS
#   <Boolean> Is the left parenthesis necessary based on adjacent operator?
#
def checkBefore(parenthesis, surrounding_operators):
    if surrounding_operators[0] in '+(' or surrounding_operators[0] == '':
        return True
    else:
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Checks if given set of parenthesis are necessary based on adjacent right operators
# PARAMETERS:
#   parenthesis <Tuple> indicies of paired parenthesis locations
#   surrounding_operators <List> operators from the left and right of paranthesis
#
# RETURNS
#   <Boolean> Is the right parenthesis necessary based on adjacent operator?
#
def checkAfter(parenthesis, surrounding_operators):
    if surrounding_operators[1] in '+-)' or surrounding_operators[1] == '':
        return True
    else:
        return False


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Orginizes each set of parenthesis by index with its surrounding operator
# PARAMETERS:
#   expression <List> valid expression
#
# RETURNS
#   <Dictionary> parenthesis indicies as keys, adjacent operators as values
#
def orginizeExpression(expression):

    orginized_expression = {}

    for i in range(0, len(expression)):
        #current parameter indexes
        stored_indicies = []
        #current adjacent operators
        stored_operators = []
        #we have reached a sub expression
        if expression[i] == '(':
            stored_indicies.append(i)
            #append left operator if exists
            if 0 <= (i - 1) < len(expression):
                stored_operators.append(expression[i - 1])
            else:
                stored_operators.append('')
            #parenthesis counter must equal zero to hit the proper closing parenthesis
            parenthesis_counter = 1
            while parenthesis_counter != 0:
                i += 1
                if expression[i] == '(':
                    parenthesis_counter += 1
                elif expression[i] == ')':
                    parenthesis_counter -= 1
            stored_indicies.append(i)
            #append right operator if exists
            if 0 <= (i + 1) < len(expression):
                stored_operators.append(expression[i + 1])
            else:
                stored_operators.append('')

            orginized_expression[tuple(stored_indicies)] = stored_operators

    return orginized_expression

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# removes unnecessary parenthesis that do not alter the expressions solution
# PARAMETERS:
#   expression <List> valid expression
#   orginized_expression <Dictionary> parenthesis indicies as keys, adjacent operators as values
#
# RETURNS
#    expression <List> expression cleaned of unecessary parenthesis
#
def cleanupParenthesis(expression, orginized_expression):

    for parenthesis in reversed(orginized_expression.keys()):
        #is the sub expression a single term OR do adjacent operators make the parenthesis necessary
        if isSingleTerm(parenthesis, expression) or (checkBefore(parenthesis, orginized_expression[parenthesis]) and checkAfter(parenthesis, orginized_expression[parenthesis])):
            expression[parenthesis[0]] = ''
            expression[parenthesis[1]] = ''

    return expression


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Checks if the expression given is valid based on paired parenthesis
# PARAMETERS:
#   expression <String> expression
#
# RETURNS
#   <Boolean> Is the expression valid based on parenthesis pairs?
#
def checkValid(expression):
    #validator must be 0 to be a valid expression
    validator = 0

    for char in expression:
        if char == '(':
            validator += 1
        elif char == ')':
            validator -= 1
    if validator == 0:
        return True
    else:
        return False

def runClient(original_expression):
    #clean up expression for optimized processing
    expression = "".join(original_expression.split())
    expression = list(expression)
    orginized_expression = orginizeExpression(expression)
    cleaned_expression_list = cleanupParenthesis(expression, orginized_expression)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the original expression is: " + str(original_expression))
    cleaned_expression_string = ''
    for char in cleaned_expression_list:
        cleaned_expression_string += char
    print("the cleaned up expression is: " + str(cleaned_expression_string))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return cleaned_expression_string



if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the unnecessary parenthesis remover!")
    print("the purpose of this program is to remove parenthesis that do not alter the solution of a valid expression when removed.")
    print('enter your valid expression as a string. for example "(4+1)" ')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    original_expression = input("Please enter an expression: ")
    #make sure the expression is valid. could be expanded to account for many things.
    is_valid = checkValid(original_expression)
    if not is_valid:
        print("Your expression is not valid")
        exit()
    runClient(original_expression)
