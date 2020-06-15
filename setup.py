
import setuptools

setuptools.setup(name="geospaas_adas_viewer",
                 version="0.1.0",
                 author=["Arash Azamifard", "Anton Korosov"],
                 description="ADAS viewer for GeoSPaaS",
                 url="https://github.com/nansencenter/django-geo-spaas-adas-viewer",
                 packages=setuptools.find_packages(),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                     "Operating System :: POSIX :: Linux",
                 ],
                 python_requires='>=3.7',
                 install_requires=['django_geo_spaas'],
                 include_package_data=True)
