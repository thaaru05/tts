from setuptools import setup, find_packages

setup(
    name='openai-tts',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        'torch',               # Assuming this is required, add any others as needed
        'transformers',        # Add any other dependencies that your code uses
        'soundfile',           # Required for audio processing
        'numpy'                # If you need it
    ],
    author='Arham KK',
    author_email='arhamkk@example.com',  # Replace with a valid email
    description='OpenAI Text-to-Speech using GPT-2',
    url='https://github.com/arham-kk/openai-tts',
)
