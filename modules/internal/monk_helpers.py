import subprocess


def handle_alternate_functionality(args, script_path):

    if args.edit:
        subprocess.run(['vim', script_path.strip()])

    if args.print:
        print(script_path.strip())
        subprocess.run(['cat', script_path.strip()])

    if args.copy_path:
        subprocess.run(['pbcopy'], input=script_path.strip().encode('utf-8'))
        print("Copied script absolute path to clipboard", 'success')

    if args.copy_contents:
        subprocess.run(['pbcopy'], input=open(script_path.strip(), 'rb').read())
        print("Copied script contents to clipboard", 'success')
