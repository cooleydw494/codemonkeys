@echo off

cd ..\..

rem Give feedback about the process.
echo Starting the setup... Hang tight! 💫

rem Check if python and pip are installed
where python >nul 2>&1
where pip >nul 2>&1
if %errorlevel% equ 0 (
    echo ✔️ Python and pip are installed. Awesome! 🐍
) else (
    echo ⚠️ Uh-oh! It seems Python or pip is not installed. Please install them and try again. 🤔
    exit /b 1
)

rem Install required python modules from requirements.txt
echo Installing required python modules... This may take a moment. ⏳
pip install -r requirements.txt

rem Create .env template
echo Creating .env template file... ✨
echo OPENAI_API_KEY=your_openai_api_key > .env

rem Use monk to generate the default configurations
echo Generating the default monkey configurations... 🐵🎛️
monk generate-monkeys

rem Feedback to the user
echo Installation finished! Woohoo! 🎉
echo You're now ready to rock 'n' roll with the 'monk' command inside this directory to run scripts in the 'scripts' directory. ✨
echo Feel free to edit the monkey configurations in the 'monkeys/monkey-manifest.yaml' file. 📝
echo To apply changes, regenerate the configurations using the command: 'monk generate-monkeys'. Keep going! 🚀

