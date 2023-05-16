import os

# Define the comments to be added
comment1 = '''
/*
  globalStyles.js Cheat Sheet:

  1. container: A base style for wrapping components, provides padding.
  2. titleText: A base style for title text, with font size, weight, and color.
  3. paragraph: A base style for paragraph text, with font size and color.
  4. input: A base style for text input, with border and padding.
  5. button: A base style for buttons, with background color, border, and padding.
  6. buttonText: A base style for button text, with font size, weight, and color.

  Usage: Import globalStyles and use the styles by referencing them, e.g., globalStyles.container.
*/'''

comment2 = '''
/*
  PostgreSQL Database Cheat Sheet:

  1. users: Stores user data including firebase_uid, email, display_name, provider, profile_picture_url, points, rewards, created_at, and updated_at.
  2. virtues: Stores the 13 virtues with their name, description, short_description, icon_name, created_at, and updated_at.
  3. user_virtues: Stores user-specific virtue data such as current_streak, longest_streak, total_days, total_successes, total_failures.
  4. daily_virtue_entries: Stores user's daily entries for each virtue with entry_date, status, notes, and rating.
  5. milestone_definitions: Stores milestone definitions with name, description, progress_requirement, icon_name, created_at, and updated_at.
  6. milestones: Stores user's achieved milestones with achieved_date.
  7. user_milestones: Stores additional details of user's milestones such as notes and rating.
  8. goals: Stores user's goals with title, description, target_date, and status.
  9. notifications: Stores user's notifications with title, message, is_read, created_at, and updated_at.
  10. weekly_focus_virtues: Stores user's weekly focus virtues with start_date and end_date.
  11. focus_virtue_entries: Stores user's entries for weekly focus virtues with entry_date, status, notes, and rating.
  12. points_log: Stores user's points log with points, description, and created_at.
  13. rewards_log: Stores user's rewards log with rewards, description, and created_at.

  Usage: Use the table and column names as needed when querying the database.
*/'''

comment3 = '''
/*
  connect.js Cheat Sheet:

  1. Import 'pg' module to access the PostgreSQL library.
  2. Import 'dotenv' module to load environment variables from the .env file.
  3. Create a new 'Pool' instance with the database connection string and SSL options.
  4. Export the 'pool' instance for use in other modules.

  Usage: Import the 'pool' instance in other modules to query the database.
*/'''

comment4 = '''
/*
VirtueMaster Directory Structure:

- App.js: Main entry point
- README.md: Documentation
- assets: Images & SVGs
  - custom-pngs: PNG files
    - logo.png: App logo (PNG)
  - custom-svgs: SVG files & components
    - BackgroundImage.js, Logo.js: SVG components
    - background-image.svg, logo.svg: SVG files
- src: App components, screens, styles & utilities
  - components: Reusable components
    - Button.js, Card.js, Header.js, ProgressChart.js, ResourceLibrary.js
  - database: DB connection & scripts
    - connect.js, createBaseTables.js, createBaseTables.sql, seedTestData.js, seedTestData.sql
  - screens: App screens
    - CommunityScreen.js, GoalsScreen.js, HomeScreen.js, ProgressScreen.js, SettingsScreen.js, SignInScreen.js, SignUpScreen.js, VirtueScreen.js, WelcomeScreen.js
  - styles: Global styles
    - globalStyles.js
  - utilities: Utility functions
    - FetchWrapper.js
  - utils: Additional utilities
    - NotificationsManager.js, pointsSystem.js
*/'''

# Define a function that appends comments to a file
def append_comments_to_file(file_path, comments):
    with open(file_path, 'a') as file:
        for comment in comments:
            file.write(comment)

# Walk through the VirtueMaster directory
for root, _, files in os.walk('./VirtueMaster'):
    for file in files:
        if file.endswith('.js'):
            file_path = os.path.join(root, file)
            append_comments_to_file(file_path, [comment1, comment2, comment3, comment4])

