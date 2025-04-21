push_ups = {
    "exercise":"Push-ups",
    "sets": 7,
    "reps": 21,
    "notes": "Keep good posture in order to get best results "
}

print(push_ups["exercise"])
print(push_ups["sets"])
print(push_ups["reps"])
print(push_ups["notes"])

#Updated the sets of exercise
push_ups["sets"] = 3

#del to delete notes
del push_ups["notes"]

#replace
push_ups["workout_notes"] = "Keep good posture in order to get best results "

print(push_ups)

#The nested dictionary
workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}
 
#Lunge notes access
print(workout_plan["Lunges"]["notes"])

# Iterating over a dictionary
# The .items() method converts the dictionary into an iterable collection of key-value pairs (tuples).
# Each tuple contains the key as the first element and the value as the second.
# We can use a for loop to access both the key and value.
for key, value in push_ups.items():
    print(f"{key.upper()}: {value}")