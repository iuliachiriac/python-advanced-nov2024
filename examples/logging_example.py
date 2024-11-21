import logging

# Step 2: Create a custom logger
logger = logging.getLogger('custom_logger')
logger.setLevel(logging.DEBUG)

# Step 3: Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Step 4: Create formatters and add them to the handlers
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s - %(message)s')

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Step 5: Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Step 6: Log messages
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')