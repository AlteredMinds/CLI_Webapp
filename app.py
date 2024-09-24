from flask import Flask, Response, request, render_template

app = Flask(__name__)

ALLOWED_USER_AGENTS = ['curl', 'wget', 'powershell']

def is_cli_user_agent(user_agent):
    for cli_agent in ALLOWED_USER_AGENTS:
        if cli_agent in user_agent.lower():
            return True
    return False
    
def get_instructions(user_agent):
    if 'curl' in user_agent.lower():
        return "\x1B[38;2;135;192;137mUse 'cls & curl https://chris.bates.contact/{route}?pass={passcode}' to navigate.\x1b[0m"
    elif 'powershell' in user_agent.lower():
        return "\x1B[38;2;135;192;137mUse 'Write-Host (Invoke-WebRequest https://chris.bates.contact/{route}?pass={passcode}).Content' to navigate.\x1b[0m"
    return ""    

HOME_TEMPLATE = """
---



\x1B[38;2;69;93;210m██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗\x1b[0m
\x1B[38;2;69;93;190m██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║\x1b[0m
\x1B[38;2;69;93;170m██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║\x1b[0m
\x1B[38;2;69;93;150m██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝\x1b[0m
\x1B[38;2;69;93;130m╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗\x1b[0m
\x1B[38;2;69;93;110m ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝\x1b[0m

\x1B[38;2;107;255;149mI'm Chris Bates, an IT student at Ozark Technical Community College pursuing a degree in Cybersecurity.
I'm passionate about technology and committed to building a career in IT and cybersecurity.\x1b[0m

\x1b[38;5;208mFeel free to explore the following routes to learn more about me and my work:\x1b[0m

> \x1b[38;5;113m/portfolio\x1b[0m     - Explore my projects
> \x1b[38;5;113m/resume\x1b[0m        - View my resume
> \x1b[38;5;113m/about\x1b[0m         - Learn more about me
> \x1b[38;5;113m/contact\x1b[0m       - Get in touch with me

\x1B[38;2;107;255;149mThank you for visiting!\x1b[0m

{instructions}
"""

PORTFOLIO_CONTENT = """
---



\x1B[38;2;69;93;210m██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ ██╗     ██╗ ██████╗ \x1b[0m
\x1B[38;2;69;93;190m██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██║     ██║██╔═══██╗\x1b[0m
\x1B[38;2;69;93;170m██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██║   ██║██║     ██║██║   ██║\x1b[0m
\x1B[38;2;69;93;150m██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║   ██║██║     ██║██║   ██║\x1b[0m
\x1B[38;2;69;93;130m██║     ╚██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝███████╗██║╚██████╔╝\x1b[0m
\x1B[38;2;69;93;110m╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═════╝ \x1b[0m


\x1B[38;2;107;255;149mWelcome to My Portfolio! Explore some of the projects I've developed over time.\x1b[0m

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mWebsites\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
> \x1b[38;5;113mhttps://github.com/AlteredMinds/QrPhishingApp\x1b[0m
   - Developed for a phishing audit experiment to educate and track user interactions with QR codes.

> \x1b[38;5;113mhttps://github.com/AlteredMinds/CLIWebapp\x1b[0m
   - The site you’re currently visiting.

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mApps\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
> \x1b[38;5;113mhttps://github.com/AlteredMinds/Calculator\x1b[0m
   - A simple calculator built with .NET and C# to challenge my programming skills.

> \x1b[38;5;113mhttps://github.com/AlteredMinds/EcoServerUtility\x1b[0m
   - An application for managing a game server I ran from home for the game ECO. created with .NET and C#.

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mScripts\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
> \x1b[38;5;113mhttp://www.planet-express.delivery/hahahash.htm\x1b[0m
   - A fun algorithm that generates a salted hash from a username and password.

> \x1b[38;5;113mhttps://github.com/AlteredMinds/OTCNetConfig\x1b[0m
   - A PowerShell script for managing network settings on school workstations.

> \x1b[38;5;113mhttps://github.com/AlteredMinds/AD_UserCreator\x1b[0m
   - A PowerShell script for creating Active Directory users with autogenerated credentials.
   
> \x1b[38;5;113mhttps://github.com/AlteredMinds/LazyWebsiteLoader\x1b[0m
   - A PowerShell script that automates the process of launching specific websites based on a user's class schedule.   

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mMiscellaneous\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
> \x1b[38;5;113mhttps://github.com/orgs/Altered-Eco-Server/repositories\x1b[0m
   - A repository of mods I created in C# for my ECO game server.
"""

RESUME_CONTENT = """
---



\x1B[38;2;69;93;210m██████╗ ███████╗███████╗██╗   ██╗███╗   ███╗███████╗\x1b[0m
\x1B[38;2;69;93;190m██╔══██╗██╔════╝██╔════╝██║   ██║████╗ ████║██╔════╝\x1b[0m
\x1B[38;2;69;93;170m██████╔╝█████╗  ███████╗██║   ██║██╔████╔██║█████╗  \x1b[0m
\x1B[38;2;69;93;150m██╔══██╗██╔══╝  ╚════██║██║   ██║██║╚██╔╝██║██╔══╝  \x1b[0m
\x1B[38;2;69;93;130m██║  ██║███████╗███████║╚██████╔╝██║ ╚═╝ ██║███████╗\x1b[0m
\x1B[38;2;69;93;110m╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝\x1b[0m


\x1B[38;2;107;255;149mChris Bates
IT Support Specialist / Cybersecurity Student
(417)771-0843 | chris@bates.contact | linkedin.com/in/chris-bat3s\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mSummary\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m

Highly motivated and detail-oriented cybersecurity student with a strong foundation in information security, programming, and troubleshooting. 
Seeking a entry level role where I can apply my technical skills and passion for problem solving to continue to learn and gain experience.

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mSkills\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m

- \x1b[38;5;113mNetwork Troubleshooting\x1b[0m     \x1B[38;2;180;180;180mResolving complex connectivity issues with knowledge of the OSI model, WAN, LAN, and VLan's.\x1b[0m
- \x1b[38;5;113mInformation Security\x1b[0m        \x1B[38;2;180;180;180mAssessing and managing security posture and Implementing zero trust architecture.\x1b[0m
- \x1b[38;5;113mProgramming & Scripting\x1b[0m     \x1B[38;2;180;180;180mExperience with Flask, HTML, JavaScript, CSS, C#, Python, Git, and PowerShell.\x1b[0m
- \x1b[38;5;113mVirtualization\x1b[0m              \x1B[38;2;180;180;180mDeploying and managing virtual machines and networks.\x1b[0m
- \x1b[38;5;113mWindows Server and Client\x1b[0m   \x1B[38;2;180;180;180mManaging DHCP, DNS, Group Policy, Hyper-V, File Shares, and Active Directory. Promoting DC and managing roles and features.\x1b[0m
- \x1b[38;5;113mLinux Systems\x1b[0m               \x1B[38;2;180;180;180mServer administration and CLI operations.\x1b[0m
- \x1b[38;5;113mCisco Networking\x1b[0m            \x1B[38;2;180;180;180mConfiguring and troubleshooting Cisco routers and switches.\x1b[0m
- \x1b[38;5;113mInterpersonal Skills\x1b[0m        \x1B[38;2;180;180;180mProven ability to build strong customer relationships and working with diverse teams.\x1b[0m

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mEducation\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
- \x1b[38;5;113mA.A.S. in Cybersecurity,\x1b[0m Ozark Technical Community College \x1B[38;2;180;180;180m(Expected 2025)\x1b[0m

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mCertifications\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
- \x1b[38;5;113mCompTIA Security+\x1b[0m
- \x1b[38;5;113mCompTIA A+\x1b[0m
- \x1b[38;5;113mTestOut Hybrid Server Pro | Core\x1b[0m \x1B[38;2;180;180;180m(proctored by instructor)\x1b[0m
- \x1b[38;5;113mCompTIA Linux+\x1b[0m \x1B[38;2;180;180;180m(currently in progress)\x1b[0m

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mExperience\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
- \x1b[38;5;113mProblem Solver, \x1b[38;5;113mAmazon\x1b[0m \x1B[38;2;180;180;180m(2023 - Present)
  \x1b[38;5;113m*\x1b[0m Troubleshoot and resolve order and package issues using critical thinking.
  \x1b[38;5;113m*\x1b[0m Use internal systems and tools to gather contexual information.
  \x1b[38;5;113m*\x1b[0m Adhere to policies and procedures to protect customer PII.
  
- \x1b[38;5;113mShift Manager, \x1b[38;5;113mHardees\x1b[0m \x1B[38;2;180;180;180m(2017 - 2023)\x1b[0m
  \x1b[38;5;113m*\x1b[0m Managed diverse teams and training new associates.
  \x1b[38;5;113m*\x1b[0m Ensuring services and products meet quality standards.  
  \x1b[38;5;113m*\x1b[0m Resolved customer issues to ensure customer satisfaction.
  \x1b[38;5;113m*\x1b[0m Optimized labor based on sales volume.
  \x1b[38;5;113m*\x1b[0m Maintained sanitation standards within the restaurant.
  
\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mAchivements\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
- \x1b[38;5;113mDean's List\x1b[0m Fall 2023, Spring 2024
- \x1b[38;5;113mPhi Theta Kappa Honor Society\x1b[0m, Member
"""

ABOUT_CONTENT = """
---



\x1B[38;2;69;93;210m █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗\x1b[0m
\x1B[38;2;69;93;190m██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝\x1b[0m
\x1B[38;2;69;93;170m███████║██████╔╝██║   ██║██║   ██║   ██║   \x1b[0m
\x1B[38;2;69;93;150m██╔══██║██╔══██╗██║   ██║██║   ██║   ██║   \x1b[0m
\x1B[38;2;69;93;130m██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║   \x1b[0m
\x1B[38;2;69;93;110m╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   \x1b[0m


\x1B[38;2;117;117;117m.................................................................................
.................................................................................
.................................................................................
................................xX$&&&&&X+X&&&$:.................................
.............................$&$X:+;;;;++++;+$&&&&&..............................
.......................X$$$$&&x:..xx;;;+++;+;X+Xx&&;$&&..........................
...................$$&$&&$$&&;+x:;;X+;;++Xx+x++$x+$&&X&&&&.......................
.................$&&$$$&&&&&;+:;;x;+$&&X$X$x+X&$X$+&&&&&&&&X.....................
.................&&$$$$&&&&&x:XxXX;+$&X+$&&$x;$&&Xx$X&&&&&&&x....................
................X&&$$&&&&&&xx&X&&&XX$XX&&X$&&$XX&&&&&&&&&&&&&:...................
................$&&&&&&$X$;$;:X$XX$$....;&$&&&;xx$&&&&&&&&&&&;...................
................XX$x+:++$;:;;;&..x:x:X;..+;::;$x$$:$;&X+x&&&&$...................
.............X$:$.x&.$X&x&;;x:..::+.$&+&&X:.::;:+&&&$X;X:;$&X&...................
...........&::x;+&x&&x.:;:$xx;:...:.:..::.::;:;;;+Xxx+$x$&+++&&&&................
...........$;+:x;$&+;;&&+;&&&&&&&&&&&&&&&&&&&&&&&&$&;$:x;+++++;;:&&..............
.........X.$;.;:xx:;::X&$;+&&&&x;:::;;::::;;;+X$&&&$X;;&::Xxx:$&&&+XX............
..........X;;:..x+x$$.&&&:........::::::::::;;++++xX$$&&&::$+:;:.&:;&............
...........Xxx$::;;+$:.....................::::;;++xx$$$&&$+x:;:X:;+x............
............;++;$&$+....::::::...............:::;+xxxXXX$$&&&&X+&;x;.............
...............&&&&x.:::::+:Xx+;.:..........:;+xxX$+X$$XXX$&&&&&&;+..............
................&&&x.:::......:.........:::::;;::;:;+X$$XX$&&&&+++...............
................:+X+..:......;+x+::....:+XX+:;;:..::;+XXXXX&&$X++................
...............:..:::..::;X.+X+x+X....:;XX$X&X.:&Xx&X+XXXXX&XX$..................
...............;..:::..:::....::;::::::;xXX$$$+;;+++xX$xxxX$Xx$..................
..................X::..:::.....:.::::::;XXXXxXXx++++xXXXXXX$&Xx..................
.................:x::::...........:::::+XXXxxxxXx++++xxXXXX$&X...................
.................:X::.............::.::;xXXXxxxx+++;++xXXXX$&X...................
..................X..............;:...:;+XXX$Xx+;++++xxxXXX&XX...................
..................$:..........::.......:+Xx+X$x::;;++xxXXXX&X....................
..................;:.........::...+::.:;X&;;x+:::;;+xxXXXXX&X....................
..............&&&&X:.........::.::;:::;:xxXXxxx;;;;+xxXXXX&X.....................
...........&&&&&&&&;:.......;::::+xx+x$xX&$XXXXXXx++xxXXX$&......................
........&&&&&&&&&&&&;::....;:+X$x$X$$&$$$$&&$&$$$XXxxxXXX&&......................
......&&&&&&$&&&&&&&Xx;::..:xxx+xx$x&$$x$&$&&&$&$&XxxX$$$&&&x....................
....&&&&&&&&&&&&&&&&&&X+::::;+++XXX$$xx$&&&&&$$XX$XXXX&&&&&&&....................
...:&&&&&&&&&&&&&&&&&&&XX+;++++++xxXxxXXXXXXXXXXX$XX$&&&&&&&&&&..................
....&&&&&&&&&&&&&&&&&&&&&$$$$x+x+xxX$&$$$$XXXXXX$&&$&&&&&&&&&&&&&xx..............
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XxxxxxxX&&&$XXXXXX$&&&&&&&&&&&&&&&&&&&&&&&&&x.......
&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&$XXxxxX$$XXXXXX$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&XXX$X$$XXX$$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&$X&&&$$$XXXXXXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&$X$&&&&$X$XXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$X$$&&&&&&&&&&&$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$X$$$$$$$$$$$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\x1b[0m

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mMy Journey in Technology\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;113mI've always been fascinated by technology. It started at a young age when my father brought home our
first computer for his business. I was immediately drawn to the command line interface – even then, 
I found it empowering to control technology with just text commands.  That early experience sparked 
a lifelong passion for programming and exploring the digital world. Throughout high school, I delved 
deeper into web development using HTML, CSS, and JavaScript.  I also explored other languages like C# 
and discovered a love for problem-solving through code. Beyond programming, computers became my creative 
outlet – I experimented with graphic design, music production, and even game modding. My passion evolved 
into a focus on cybersecurity. The challenge of protecting information and systems in our increasingly 
digital world excites me. This led me to pursue a degree in Cybersecurity at Ozark Technical Community 
College in Springfield, Missouri.\x1b[0m

\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mLooking Ahead\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;113mI'm eager to apply my knowledge and gain practical experience through internships or entry-level positions.  
I'm particularly interested in roles that focus on Cybersecurity. 

If you have any opportunities or would like to get in contact, please feel free to reach out to me via 
email at chris@bates.contact or connect with me on LinkedIn at linkedin.com/in/chris-bat3s.\x1b[0m
"""

CONTACT_CONTENT = """
---



\x1B[38;2;69;93;210m ██████╗ ██████╗ ███╗   ██╗████████╗ █████╗  ██████╗████████╗\x1b[0m
\x1B[38;2;69;93;190m██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝\x1b[0m
\x1B[38;2;69;93;170m██║     ██║   ██║██╔██╗ ██║   ██║   ███████║██║        ██║   \x1b[0m
\x1B[38;2;69;93;150m██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██║██║        ██║   \x1b[0m
\x1B[38;2;69;93;130m╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╗   ██║   \x1b[0m
\x1B[38;2;69;93;110m ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝   \x1b[0m


- \x1b[38;5;113mPhone:\x1b[0m [Phonenumber]
- \x1b[38;5;113mEmail:\x1b[0m chris@bates.contact
- \x1b[38;5;113mGPG Key:\x1b[0m https://chris.bates.contact/pubkey
\x1B[38;2;117;117;117m===================================================================\x1b[0m
\x1b[38;5;208mSocial\x1b[0m
\x1B[38;2;117;117;117m===================================================================\x1b[0m
- \x1b[38;5;113mLinkedIn:\x1b[0m linkedin.com/in/chris-bat3s
- \x1b[38;5;113mGithub:\x1b[0m Github.com/AlteredMinds
"""

KEY_CONTENT = """\x1B[2J-----BEGIN PGP PUBLIC KEY BLOCK-----

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
qA2zQhycY+k3NXlREku4v5NtSGrVY6tTQg==
=BqYQ
-----END PGP PUBLIC KEY BLOCK-----
"""

ERROR_CONTENT = """Command unrecognized. Please check your command and try again. 
"""

DENIED_CONTENT = """You are unauthorized to access this content. Please provide the passcode.
"""

def is_authorized(id):
    valid_id = "secret_passcode"
    return id == valid_id

@app.route('/')
@app.route('/h')
@app.route('/ho')
@app.route('/hom')
@app.route('/home')
def home():
    user_agent = request.headers.get('User-Agent')
    if not is_cli_user_agent(user_agent):
        return render_template('denied.html')       
    
    instructions = get_instructions(user_agent)
    home_ascii_art = HOME_TEMPLATE.format(instructions=instructions)
    
    return Response(home_ascii_art, mimetype='text/plain')

@app.route('/po')
@app.route('/por')
@app.route('/port')
@app.route('/portf')
@app.route('/portfo')
@app.route('/portfol')
@app.route('/portfoli')
@app.route('/portfolio')
def blog():
    user_agent = request.headers.get('User-Agent')
    if not is_cli_user_agent(user_agent):
        return render_template('denied.html')
    id = request.args.get('pass')    
    if not is_authorized(id):
        return Response(DENIED_CONTENT, mimetype='text/plain')
        
    return Response(PORTFOLIO_CONTENT, mimetype='text/plain')

@app.route('/r')
@app.route('/re')
@app.route('/res')
@app.route('/resu')
@app.route('/resum')
@app.route('/resume')
def resume():
    user_agent = request.headers.get('User-Agent')
    if not is_cli_user_agent(user_agent):
        return render_template('denied.html')
    id = request.args.get('pass')    
    if not is_authorized(id):
        return Response(DENIED_CONTENT, mimetype='text/plain')
        
    return Response(RESUME_CONTENT, mimetype='text/plain')

@app.route('/a')
@app.route('/ab')
@app.route('/abo')
@app.route('/abou')
@app.route('/about')
def about():
    user_agent = request.headers.get('User-Agent')
    if not is_cli_user_agent(user_agent):
        return render_template('denied.html')
    id = request.args.get('pass')    
    if not is_authorized(id):
        return Response(DENIED_CONTENT, mimetype='text/plain')
        
    return Response(ABOUT_CONTENT, mimetype='text/plain')

@app.route('/c')
@app.route('/co')
@app.route('/con')
@app.route('/cont')
@app.route('/conta')
@app.route('/contac')
@app.route('/contact')
def contact():
    user_agent = request.headers.get('User-Agent')
    if not is_cli_user_agent(user_agent):
        return render_template('denied.html')
    id = request.args.get('pass')    
    if not is_authorized(id):
        return Response(DENIED_CONTENT, mimetype='text/plain')
        
    return Response(CONTACT_CONTENT, mimetype='text/plain')    

@app.route('/pu')
@app.route('/pub')
@app.route('/pubk')
@app.route('/pubke')
@app.route('/pubkey')
def pubkey():
    user_agent = request.headers.get('User-Agent')
    if not is_cli_user_agent(user_agent):
        return render_template('denied.html')
    return Response(KEY_CONTENT, mimetype='text/plain') 

@app.errorhandler(404)
def page_not_found(e):
    user_agent = request.headers.get('User-Agent')
    if not is_cli_user_agent(user_agent):
        return render_template('denied.html')
    return Response(ERROR_CONTENT, mimetype='text/plain')  

if __name__ == '__main__':
    app.run()	