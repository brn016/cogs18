

class Variable():
    """Class to store information about variables."""
    
    def __init__(self, name, is_mutable, is_collection):
        """
        
        Parameters
        ----------
        name : str
            The name of the variable.
        is_mutable : boolean
            Whether the variable is mutable or not.
        is_collection : boolean
            Whether the variable is a collection or not.
        """
        
        self.name = name
        self.is_mutable = is_mutable
        self.is_collection = is_collection
        
    def get_info(self):
        """Returns information about the instance.
        
        Returns
        -------
        string
            The result of whether the instance is mutable or a collection. 
        """
        
        if self.is_mutable == True and self.is_collection == True:
            return(self.name + ' is a collection, and it is mutabel.')
        elif self.is_mutable == True and self.is_collection == False:
            return(self.name + ' is not a collection, but it is mutable.')
        elif self.is_mutable == False and self.is_collection == True:
            return(self.name + ' is a collection, but it is not mutable.')
        else:
            return(self.name + ' is neither mutable nor a collection.')

        
class Operator():
    """Class to store information about operators."""
    
    def __init__(self, name, math_operator, comparison_operator, boolean_logic, assign_operator):
        """
        
        Parameters
        ----------
        name : str
            The name of the operator.
        math_operator : boolean
            Whether the operator is a math operator or not.
        comparison_operator : boolean
            Whether the operator is a comparison operator or not.
        boolean_logic : boolean
            Whether the operator is for boolean logic or not.
        assign_operator : boolean
            Whether the operator is for assignment or not. 
        """
        
        self.name = name
        self.math_operator = math_operator
        self.comparison_operator = comparison_operator
        self.boolean_logic = boolean_logic
        self.assign_operator = assign_operator
      
    def get_info(self):
        """Returns information about the instance.
        
        Returns
        -------
        string
            The kind of the instance and what it returns. 
        """
        
        if self.math_operator == True:
            return(self.name + ' is a mathematical operator and it returns number.')
        elif self.comparison_operator == True:
            return(self.name + ' is a comparison operator and it returns boolean.')
        elif self.boolean_logic == True:
            return(self.name + ' is for boolean logic and it returns boolean.')
        else:
            return(self.name + ' is for assignment.')    

        
class Conditionals():
    """Class to store information about conditionals."""
    
    def __init__(self, name):
        """
        
        Parameters
        ----------
        name : str
            The name of the conditionals. 
        """
        
        self.name = name
    
    def get_info(self):
        """Returns information about the instance.
        
        Returns
        -------
        string
            The defination the instance. 
        """
        
        if self.name == 'if':
            return('Using the `if` statement check for a condition, and then only execute a set of code if the condition evaluates as True.')
        elif self.name == 'else':
            return('After an `if`, you can use an `else` that will run if the conditional(s) above have not run.')
        else:
            return('After an if statement, you can have any number of `elif` to check other conditions.')
        
        
class Loops():
    """Class to store information about loops."""
    
    def __init__(self, name):
        """
        
        Parameters
        ----------
        name : str
            The name of the loop and relating operation. 
        """
        
        self.name = name 
        
    def get_info(self):
        """Returns information about the instance.
        
        Returns
        -------
        string
            The defination the instance. 
        """
        
        if self.name == 'while loop':
            return('A while loop is a procedure to repeat a piece of code while some condition is still met.')
        elif self.name == 'for loop':
            return('A for loop is a procedure a to repeat code for every element in a sequence.')
        elif self.name == 'range':
            return('`range` is an operator to create a range of numbers, that is often used with loops.')
        elif self.name == 'continue':
            return('`continue` is a special operator to jump ahead to the next iteration of a loop.')
        else:
            return('`break` is a special operator to break out of a loop.')

        
class Errors():
    """Class to store information about Errors."""
    
    def __init__(self, name):
        """
        
        Parameters
        ----------
        name : str
            The name of the error. 
        """
        
        self.name = name 
        
    def get_info(self):
        """Returns information about the instance.
        
        Returns
        -------
        string
            The defination the instance. 
        """
        
        if self.name == 'Syntax & Indentation Errors':
            return('Syntax & Indentation Errors reflect code that does not follow Python structure, and will necessarily fail.')
        elif self.name == 'ZeroDivisionError':
            return('ZeroDivisionError occurs when you try to divide by zero.')
        elif self.name == 'NameError':
            return('NameError occurs when you try to access a name that Python does not know.')
        elif self.name == 'IndexError':
            return('IndexError occurs when you try to access an index that doesn’t exist.')
        elif self.name == 'ValueError':
            return('ValueError occurs when you try to use an illegal value for something.')
        else:
            return('A TypeError occurs when an operation or function is applied to an object of inappropriate type.')
           