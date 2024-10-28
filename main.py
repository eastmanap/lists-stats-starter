# Apollos Eastman
# 10/28
# Lists Stats

print()
# Quiz Scores
scores = [89,58,96,10,68]

average = sum(scores)/len(scores)

print(f'Your average is score was {average:.2f}.\n')

# Driving Distances
locations, distances = ['Detroit','Grand Rapids', 'Mio', 'Lansing','Frankfort'], [256,142,82,182,42]

#Shortest trip
short_trip = min(distances)
short_loc = distances.index(short_trip)

#Longest trip
long_trip = max(distances)
long_loc = distances.index(long_trip)

#Average length
average_trip = sum(distances)/len(distances)

print(f'The shortest trip is to {locations[short_loc]} which is {short_trip:.2f} miles.')
print(f'The longest trip is to {locations[long_loc]} which is {long_trip:.2f} miles.')
print(f'The average distance of the five locations was {average_trip:.2f} miles.\n')
