from setuptools import setup

setup(name='gclid-timestamp-decoder',
      version='0.1.3',
      description='Decoding timestamp from Google gclid using Protocol Buffers.',
      author='Kenny Shen',
      author_email='kenny@machinesung.com',
      license='BSD',
      url='https://github.com/jezzarax/gclid-timestamp-decoder',
      install_requires=['protobuf>=3.0'],
      packages=['gclid_timestamp_decoder']
    )
