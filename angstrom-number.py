from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title and font
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Weekly Gym Routine for Strength & Physique", ln=True, align='C')

# Add space
pdf.ln(10)

# Gym Day Weekly Routine with Exercises
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="1. Gym Day Weekly Routine for Strength & Physique", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
- **Monday**: Chest & Triceps
    - **Chest**:
      - Bench Press (4 sets of 8-10 reps)
      - Incline Dumbbell Press (4 sets of 8-10 reps)
      - Chest Flys (3 sets of 10-12 reps)
    - **Triceps**:
      - Triceps Dips (4 sets of 8-10 reps)
      - Triceps Pushdowns (3 sets of 10-12 reps)
      - Overhead Triceps Extension (3 sets of 10-12 reps)

- **Tuesday**: Back & Biceps
    - **Back**:
      - Deadlifts (4 sets of 6-8 reps)
      - Barbell Rows (4 sets of 8-10 reps)
      - Lat Pulldowns (4 sets of 8-10 reps)
      - T-Bar Rows (3 sets of 10-12 reps)
    - **Biceps**:
      - Barbell Curls (4 sets of 8-10 reps)
      - Hammer Curls (3 sets of 10-12 reps)
      - Preacher Curls (3 sets of 10-12 reps)

- **Wednesday**: Legs & Core
    - **Legs**:
      - Squats (4 sets of 8-10 reps)
      - Leg Press (4 sets of 8-10 reps)
      - Lunges (3 sets of 10-12 reps per leg)
      - Leg Curls (3 sets of 10-12 reps)
      - Leg Extensions (3 sets of 10-12 reps)
    - **Core**:
      - Planks (3 sets of 1-2 minutes)
      - Leg Raises (3 sets of 15-20 reps)
      - Russian Twists (3 sets of 20 reps per side)

- **Thursday**: Shoulders & Abs
    - **Shoulders**:
      - Overhead Press (4 sets of 8-10 reps)
      - Lateral Raises (4 sets of 12-15 reps)
      - Front Raises (3 sets of 10-12 reps)
      - Rear Delt Flys (3 sets of 10-12 reps)
    - **Abs**:
      - Cable Crunches (3 sets of 12-15 reps)
      - Hanging Leg Raises (3 sets of 10-12 reps)
      - Russian Twists (3 sets of 20 reps per side)
      - Ab Wheel Rollouts (3 sets of 10-12 reps)

- **Friday**: Full Body & Cardio
    - **Full Body**:
      - Deadlifts (4 sets of 6-8 reps)
      - Bench Press (4 sets of 8-10 reps)
      - Squats (4 sets of 8-10 reps)
      - Barbell Rows (4 sets of 8-10 reps)
    - **Cardio**:
      - 30 minutes of moderate-intensity cardio (e.g., treadmill, cycling, or rowing)

- **Saturday**: Rest or Active Recovery
    - Focus on light stretching, yoga, or a walk to promote muscle recovery.
    - Foam rolling to help with muscle soreness.

- **Sunday**: Optional Light Cardio or Rest
    - Optional light cardio session, such as a walk, jog, or cycling for 20-30 minutes.
    - Full rest day if you feel fatigued.
""")

# Add space
pdf.ln(5)

# Explanation of Routine
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Explanation of the Weekly Gym Routine:", ln=True)
pdf.ln(5)

pdf.multi_cell(0, 10, """
1. **Chest & Triceps (Monday)**:
    - **Chest Exercises**: Compound movements like the Bench Press and Incline Dumbbell Press help build overall mass and strength in the chest. Chest Flys isolate the chest muscles for better definition.
    - **Triceps Exercises**: Triceps Dips and Pushdowns focus on building the triceps, which are crucial for improving pushing movements. The overhead extension targets the long head of the triceps for better size.

2. **Back & Biceps (Tuesday)**:
    - **Back Exercises**: Deadlifts are a powerful full-body lift that also strengthens the back. Lat Pulldowns and Barbell Rows target the lats, traps, and rhomboids, while T-Bar Rows build thickness in the middle of the back.
    - **Biceps Exercises**: Barbell Curls and Hammer Curls focus on bicep strength and size. Preacher Curls isolate the biceps for better definition.

3. **Legs & Core (Wednesday)**:
    - **Leg Exercises**: Squats and Leg Press are the best exercises for overall leg strength and muscle mass. Lunges help improve balance and target the quads and glutes. Leg Curls and Extensions work the hamstrings and quads.
    - **Core Exercises**: Planks and Leg Raises build core strength, while Russian Twists target the obliques, helping you improve your posture and overall strength.

4. **Shoulders & Abs (Thursday)**:
    - **Shoulders Exercises**: Overhead Press and Lateral Raises build the deltoids, while Front Raises and Rear Delt Flys work on shoulder stability and definition.
    - **Abs Exercises**: Cable Crunches and Hanging Leg Raises are great for targeting the upper and lower abs. Ab Wheel Rollouts engage your entire core for better stability.

5. **Full Body & Cardio (Friday)**:
    - **Full Body Exercises**: Combining Deadlifts, Bench Press, Squats, and Barbell Rows will engage all major muscle groups, helping you improve overall strength and physique.
    - **Cardio**: Doing cardio post-strength training helps with fat loss and cardiovascular fitness.

6. **Rest or Active Recovery (Saturday)**:
    - Active recovery is essential for muscle growth. Stretching and yoga help keep your muscles flexible, while foam rolling helps alleviate muscle soreness.

7. **Optional Light Cardio or Rest (Sunday)**:
    - An optional light cardio session helps keep your body active without putting too much strain on the muscles. However, it's important to rest if you're feeling fatigued.

""")

# Save the PDF to a file
file_path = "Weekly_Gym_Routine_for_Strength_and_Physique_with_Exercises.pdf"
pdf.output(file_path)

file_path  # Return the file path for download.
