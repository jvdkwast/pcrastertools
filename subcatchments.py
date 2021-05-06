from pcraster import *

DEM = readmap('dem.map')
FlowDirection = readmap('ldd.map')
threshold = 8

# print('Calculating flow direction')
# FlowDirection = lddcreate(DEM,1e31,1e31,1e31,1e31)
# report(FlowDirection,'ldd.map')

print('Calculating Strahler orders')
StrahlerOrders = streamorder(FlowDirection)
StrahlerRivers = ifthen(StrahlerOrders >= threshold, StrahlerOrders)

print('Finding outlets')
Junctions = ifthen(downstream(FlowDirection,StrahlerRivers) != StrahlerRivers,boolean(1))
Outlets = ordinal(cover(uniqueid(Junctions),0))

print('Calculate subcatchments')
# SubCatchments = catchment(FlowDirection,Outlets)
# report(SubCatchments,'subcatchments.map')
# aguila(SubCatchments)
MaximumOutlets = mapmaximum(Outlets)
MaximumOutletsTuple = cellvalue(MaximumOutlets,0,0)
MaximumOutletsValue = MaximumOutletsTuple[0]
print('Total subcatchments:', MaximumOutletsValue)

for outlet in range(1,MaximumOutletsValue + 1):
    print('\rProcessing subcatchment', outlet, end='', flush=True),
    SubCatchment = catchment(FlowDirection,ifthenelse(Outlets == outlet,boolean(1),boolean(0)))
    report(SubCatchment,'subcatchment'+str(outlet)+'.map')
    aguila(SubCatchment)
    
print('\nDone')
