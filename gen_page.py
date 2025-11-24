from jinja2 import Environment, FileSystemLoader
import os
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')

filename = os.path.join(root, 'index.html')

temp = {'title': '',
        'author': '',
        'description': '',
        'badges': [],
        'link': ''}

all_resources = {
    'Blog Series': [
        {'title': 'DifferentialPrivacy.org',
         'author': 'Various',
         'description': 'A blog with many DP resources, aimed at a variety of audiences.',
         'badges': ['Technical', 'Somewhat Technical', 'Blog Posts'],
         'link': 'https://differentialprivacy.org/'},

        {'title': 'A friendly, non-technical introduction to differential privacy',
         'author': 'Damien Desfontaines',
         'description': 'A friendly blog post series about differential privacy! It provides simple explanations for the core concepts behind differential privacy. It is meant for a wide, non-technical audience: it doesn\'t assume any prior knowledge, uses as little math as possible, and illustrates everything with simple examples and diagrams.',
         'badges': ['Somewhat Technical', 'Blog Posts'],
         'link': 'https://desfontain.es/privacy/friendly-intro-to-differential-privacy.html'},

        {'title': 'NIST Differential Privacy Blog Series',
         'author': 'Various',
         'description': 'This series is designed to help business process owners and privacy program personnel understand basic concepts about differential privacy and applicable use cases and to help privacy engineers and IT professionals implement the tools. ',
         'badges': ['Somewhat Technical', 'Blog Posts'],
         'link': 'https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/collaboration-space/blog-series/differential-privacy'}
        ],

    'Courses': [

        {'title': 'CS 860 - Algorithms for Private Data Analysis',
         'author': 'Gautam Kamath',
         'description': 'This course is on algorithms for differentially private analysis of data. As necessitated by the nature of differential privacy, this course will be theoretically and mathematically based. References to practice will be provided as relevant, especially towards the end of the course. Prerequisites include an undergraduate understanding of algorithms, comfort with probability, and mathematical maturity.',
         'badges': ['Technical', 'Course Notes', 'Videos'],
         'link': 'http://www.gautamkamath.com/CS860-fa2020.html'},

        {'title': 'Privacy in Statistics and Machine Learning',
         'author': 'Adam Smith, Jonathan Ullman',
         'description': 'How can we learn from a data set of sensitive information while providing meaningful privacy to the individuals whose information it contains? The course explores this question, starting from the problems faced by straightforward solutions and moving on to rigorous state-of-the-art solutions using differential privacy. The class will focus on foundations, but also delve into some applied work and on some of the social, ethical, and legal context for the subject. Students will be required to complete some mathematical assignments, some light programming assignments, and a final course project.',
         'badges': ['Technical', 'Course Notes', 'Videos'],
         'link': 'https://dpcourse.github.io/'},

        {'title': 'CS 208 - Applied Privacy for Data Science',
         'author': 'Salil Vadhan, James Honaker, Wanrong Zhang',
         'description': 'The risks to privacy when making human subjects data available for research and how to protect against these risks using the formal framework of differential privacy. Methods for attacking statistical data releases, the mathematics of and software implementations of differential privacy, deployed solutions in industry and government. Assignments will include implementation and experimentation on data science tasks.',
         'badges': ['Technical', 'Course Notes'],
         'link': 'https://opendp.github.io/cs208/'}
    ],

    'Books & Articles': [
        {'title': 'The Algorithmic Foundations of Differential Privacy',
         'author': 'Cynthia Dwork, Aaron Roth',
         'link': 'https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf',
         'description': 'A thorough introduction to the problems and techniques of differential privacy, including theoretical foundations, fundamental techniques, and applications.',
         'badges': ['Somewhat technical'],
         },

        {'title': 'Hands-On Differential Privacy',
         'author': 'Ethan Cowan, Michael Shoemate, Mayana Pereira',
         'link': 'https://www.oreilly.com/library/view/hands-on-differential-privacy/9781492097730/',
         'description': "Explains how differential privacy enables data scientists, researchers, and programmers to run statistical analyses that hide the contribution of any single individual. You'll dive into basic DP concepts and understand how to use open source tools to create differentially private statistics, explore how to assess the utility/privacy trade-offs, and learn how to integrate differential privacy into workflows.",
         'badges': ['Coders']
         },

        {'title': 'Designing Access with Differential Privacy',
         'author': 'Alexandra Wood, Micah Altman, Kobbi Nissim, Salil Vadhan',
         'link': 'https://admindatahandbook.mit.edu/book/v1.0/diffpriv.html',
         'description': 'A (shorter) successor to the Non-technical Primer on Differential Privacy, with a more operational focus on helping policymakers and others think broadly about deploying differential privacy.',
        'badges': ['Non-technical'],
        },

        {'title': 'A Non-technical Primer on Differential Privacy',
         'author': 'Alexandra Wood, Micah Altman, Aaron Bembenek, Mark Bun, Marco Gaboardi, James Honaker, Kobbi Nissim, David R. O\'Brien, Thomas Steinke & Salil Vadhan',
         'link': 'https://salil.seas.harvard.edu/sites/scholar.harvard.edu/files/salil/files/differential_privacy_primer_nontechnical_audience.pdf',
         'description': 'This primer seeks to introduce the concept of differential privacy and its privacy implications to non-technical audiences. It provides a simplified and informal, but mathematically accurate, description of differential privacy.',
         'badges': ['Non-technical'],
         },

        {'title': 'The Complexity of Differential Privacy',
         'author': 'Salil Vadhan',
         'link': 'https://link.springer.com/chapter/10.1007/978-3-319-57048-8_7',
         'description': 'Aimed at theoretical computer scientists who want to engage with theoretical research on differential privacy.',
         'badges': ['Technical'],
        }

    ],

    'Tutorials': [

        {'title': 'Tumult Analytics tutorials',
         'author': 'Tumult Labs',
         'link': 'https://docs.tmlt.dev/analytics/latest/tutorials/index.html',
         'description': 'A tutorial series from Tumult Analytics, intended to get started generating differentially private data without any prior experience with DP.',
         'badges': ['For Coders'],
         },

        {'title': 'Exploring Differential Privacy: Laplace vs Gaussian',
         'author': 'Liudas Panavas',
         'link': 'https://lpanavas.github.io/mechanism-comparison/',
         'description': 'A visualization of the utility tradeoffs between the Laplace and Gaussian mechanisms.',
         'badges': [],
        },
        ]

    }

with open(filename, 'w') as fh:
    fh.write(template.render(
        all_resources = all_resources
    ))
