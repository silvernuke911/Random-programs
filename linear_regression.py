import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

def execution_time(func):
    """
    Decorator to measure and print the time taken by a function to execute.

    Parameters:
        func (callable): The function to be decorated.

    Returns:
        callable: Decorated function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Execution time of '{func.__name__}': {execution_time:.6f} seconds")
        return result
    return wrapper

def mean_square_error(y_observed,y_predicted):
    if len(y_observed)!=len(y_predicted):
        raise ValueError('Input length not equal')
    n=len(y_observed)
    output=(1/n)*np.sum(np.square(y_predicted-y_observed))
    return output

@execution_time
def r2(x, y, pred_func):
    """
    Evaluate how well the prediction function predicts the behavior of y based on x.

    Parameters:
    x (array-like): An array of x-values.
    y (array-like): An array of y-values.
    pred_func (function): A function that takes x as input and returns predicted y-values.

    Returns:
    float: The R^2 value indicating how well the function predicts y.
    
    Raises:
    ValueError: If the lengths of x and y are not equal.
    """
    # Check if the lengths of x and y are equal
    if len(x) != len(y):
        raise ValueError('input length not equal')
    # Convert x and y to numpy arrays for easier manipulation
    x = np.array(x)
    y = np.array(y)
    # Get the predicted y values using the prediction function
    y_pred = pred_func(x)
    # Calculate the total sum of squares (SST)
    y_mean = np.mean(y)
    ss_total = np.sum((y - y_mean) ** 2)
    # Calculate the residual sum of squares (SSR)
    ss_residual = np.sum((y - y_pred) ** 2)
    # Calculate the R^2 value
    r2 = 1 - (ss_residual / ss_total)
    return r2

@execution_time
def r_squared(x,y,function):
    if len(x) != len(y):
        raise ValueError('Input length not equal')
    y_pred = function(x)
    ssr = np.sum(np.square(y-y_pred))
    sst = np.sum(np.square(y-np.mean(y)))
    r2=1-ssr/sst
    return r2

def plot():
    def lims(x):
        ave=(np.max(x)+np.min(x))/2
        ran=abs(np.max(x)-np.min(x))
        return [ave-ran*0.75,ave+ran*0.75]
    x_min,x_max=lims(x)
    y_min,y_max=lims(y)
    plt.grid()
    plt.axis([x_min,x_max, y_min, y_max])
    plt.scatter(x,y,marker='.',color='red')
    plt.plot(np.linspace(x_min,x_max,2),[m*x+b for x in np.linspace(x_min,x_max,2)])
    plt.show()

# def loss_function(x_list,y_list,m,b,points):
#     total_error=0
#     for i in range(len(points)):
#         x=x_list[i]
#         y=y_list[i]
#         total_error+= (y-(m*x+b))**2
#     total_error/float(len(points))

# def gradient_descent(x_list,y_list,m_now,b_now,learning_rate,intercept0=False):
#     m_gradient=0
#     b_gradient=0
#     n=len(x_list)
#     for i in range(n):
#         x=x_list[i]
#         y=y_list[i]
#         m_gradient+=-(2/n)*x*(y-(m_now*x+b_now))
#         if intercept0==False:
#             b_gradient+=-(2/n)*(y-(m_now*x+b_now))
#         else:
#             b_gradient=0
#     m=m_now-m_gradient*learning_rate
#     b=b_now-b_gradient*learning_rate
#     return m,b

# def linear_regression(x,y,m=0,b=0,L=0.01,intercept0=True,max_iter=10000,tol=1e-10):
#     for _ in range(max_iter):
#         m_new,b_new=gradient_descent(x,y,m,b,L,intercept0)
#         error=abs(np.sqrt((m_new-m)**2+(b_new-b)**2))
#         if error<tol:
#             break
#         m,b=m_new,b_new
#         print(f'{m} {b} {error} {_}'+'   ',end='\r',sep=' ')
#     return [m,b]

# def output_equation(m,b,rnd=15):
#     if b==0:
#         return str(round(m,rnd))+'x'
#     return 'y='+str(round(m,rnd))+'x+'+str(round(b,rnd))



# def loss_function(x_list, y_list, m, b):
#     """
#     Compute the mean squared error between actual y values and predicted y values using the linear equation y = mx + b.
#     """
#     # Compute the total error using vectorized operations for efficiency
#     total_error = np.sum((y_list - (m * x_list + b))**2)
#     # Return the mean error
#     return total_error / len(x_list)

# def gradient_descent(x_list, y_list, m_now, b_now, learning_rate, intercept0=False):
#     """
#     Perform a single step of gradient descent to update the slope (m) and intercept (b) of the linear model.
#     """
#     # Compute the gradient for m using vectorized operations
#     m_gradient = np.mean(-2 * x_list * (y_list - (m_now * x_list + b_now)))
#     # Compute the gradient for b, or set it to 0 if intercept0 is True
#     if intercept0:
#         b_gradient = 0
#     else:
#         b_gradient = np.mean(-2 * (y_list - (m_now * x_list + b_now)))
    
#     # Update m and b using the computed gradients and the learning rate
#     m = m_now - m_gradient * learning_rate
#     b = b_now - b_gradient * learning_rate
#     return m, b

# def linear_regression(x, y, m, b, L=0.01, intercept0=False, max_iter=10000, tol=1e-10):
#     """
#     Fit a linear regression model to the data using gradient descent.
#     """
#     for _ in range(max_iter):
#         # Perform a step of gradient descent
#         m_new, b_new = gradient_descent(x, y, m, b, L, intercept0)
        
#         # Calculate the change in parameters
#         error = np.sqrt((m_new - m)**2 + (b_new - b)**2)
        
#         # Check for convergence
#         if error < tol:
#             break
        
#         # Update parameters
#         m, b = m_new, b_new
        
#         # Print the current parameters and error
#         print(f'{m} {b} {error} {_}' + '   ', end='\r')
    
#     # Return the final parameters
#     return m, b

@execution_time
def linear_regression(x, y, intercept_0=False):
    """
    Calculate the best fit line for the given x and y data points using linear regression.
    
    Parameters:
    x (array-like): An array of x-values.
    y (array-like): An array of y-values.
    intercept_0 (bool): If True, forces the y-intercept (b) to be 0. Default is False.
    
    Returns:
    tuple: A tuple containing the slope (m) and y-intercept (b) of the best fit line.

    Raises:
    ValueError: If the lengths of x and y are not equal.
    """
    # Check if the lengths of x and y are equal
    if len(x) != len(y):
        raise ValueError('Input length not equal')
    
    # Convert x and y to numpy arrays for easier manipulation
    x = np.array(x)
    y = np.array(y)
    
    if intercept_0:
        # When intercept is forced to be 0, calculate slope directly
        m = np.sum(x * y) / np.sum(x ** 2)
        b = 0
    else:
        # Calculate the mean of x and y
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        
        # Calculate the terms needed for the numerator and denominator of the slope (m)
        numerator = np.sum((x - x_mean) * (y - y_mean))
        denominator = np.sum((x - x_mean) ** 2)
        
        # Calculate the slope (m)
        m = numerator / denominator
        
        # Calculate the y-intercept (b)
        b = y_mean - m * x_mean
    
    return m, b

def exponential_fit(x, y):
    from scipy.optimize import curve_fit
    # Define the exponential function to fit
    def model(x, A, B, C):
        return A * np.exp(B * x) + C

    # Use curve_fit to find the best-fit parameters
    popt, pcov = curve_fit(model, x, y, p0=(1, 1, 1))

    # Extract the parameters A, B, and C
    A, B, C = popt

    return A, B, C
    
def logarithmic_fit(x, y):
    from scipy.optimize import curve_fit
    # Define the logarithmic function to fit
    def model(x, A, B, C):
        return A * np.log(x + B) + C

    # Provide an initial guess for A, B, and C
    initial_guess = (1, 1, 1)
    
    # Use curve_fit to find the best-fit parameters
    popt, pcov = curve_fit(model, x, y, p0=initial_guess)

    # Extract the parameters A, B, and C
    A, B, C = popt

    return A, B, C

def polynomial_regression(x, y, n):
    """
    Calculate the coefficients of the best fit polynomial of the nth order for the given x and y data points.
    
    Parameters:
    x (np.array): An array of x-values.
    y (np.array): An array of y-values.
    n (int): The order of the polynomial.
    
    Returns:
    np.array: An array of coefficients of the polynomial, starting with the highest degree.
    
    Raises:
    ValueError: If the lengths of x and y are not equal.
    """
    # Check if the lengths of x and y are equal
    if len(x) != len(y):
        raise ValueError('input length not equal')
    
    # Calculate the polynomial coefficients
    coefficients = np.polyfit(x, y, n)
    
    return coefficients

def output_equation(m, b, rnd=15):
    """
    Generate a string representation of the linear equation y = mx + b with rounded coefficients.
    """
    # Round the coefficients
    m_rounded = np.round(m, rnd)
    b_rounded = np.round(b, rnd)
    
    if b_rounded<0:
        sgn='-'
    else: sgn='+'
    # Check if b is close to zero for numerical stability
    if np.isclose(b, 0):
        return f"y = {m_rounded}x"
    
    # Return the equation as a string
    return f"y = {m_rounded}x {sgn} {abs(b_rounded)}"

def initial_fit(x,y):
    """
    Generates the initial slope and y-intercept of a given linear data set by calculating the slope and y-intercept of the first and last point.
    """

    m=(y[-1]-y[0])/(x[-1]-x[0])
    b=y[0]-m*x[0]
    return m,b

data = pd.read_csv('plotto.csv',sep='\t')
print(data)

x=np.array(data.c_e)
y=np.array(data.m_p)
# import random
# x=np.arange(0,50,1)
# for i in range(len(x)):
#     x[i]=x[i]+10*random.random()
# y=np.arange(0,50,1)
# for i in range(len(y)):
#     y[i]=y[i]+10*random.random()
# x=np.array(data.a)
# y=np.array(data.b)
m_i,b_i=initial_fit(x,y)
slope_i=linear_regression(x,y,False)
m,b=slope_i[0],slope_i[1]
print() 
print(output_equation(m,b,3))

def fit_func(x):
    return m*x+b
y_pred=fit_func(x)
print(f'R^2 = {r_squared(x,y,fit_func):.3f}')

plot()


