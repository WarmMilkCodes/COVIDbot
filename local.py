import addfips


county = 'lawrence'
stateIn = 'mo'

af = addfips.AddFIPS()
print(af.get_county_fips(county, state=stateIn))
fips = af.get_county_fips('lawrence', state='Missouri')
print(fips)

