from django.shortcuts import render
from .models import thesis_projects
# Create your views here.

"""
thesis1 = thesis_projects()
thesis1.topic_num = 1
thesis1.title = 'Machine learning approaches for Cyber Security'
thesis1.description = 'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction andfor an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.'
thesis1.superviser = 'Bharanidharan Shanmugam'


thesis2 = thesis_projects()
thesis2.topic_num = 9
thesis2.title = 'Informetrics applications in multidisciplinary domain'
thesis2.description = 'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniqueson various information artefact have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary researchliterature using various machine learning, network analysis, data visualisation and data wrangling tools.'
thesis2.superviser = 'Yakub Sebastian'


thesis3 = thesis_projects()
thesis3.topic_num = 16
thesis3.title = 'Development of a Virtual Reality System to Test Binaural Hearing'
thesis3.description ='A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design,implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.'
thesis3.superviser ='Sami Azam'


thesis4 = thesis_projects()
thesis4.topic_num = 41
thesis4.title = 'Current trends on cryptomining and its potential impact on cryptocurrencies'
thesis4.description ="Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computersand spend a lot of time and money running them to perform the difficult calculations to generate crypto coins. Some website owners have started taking a different approach; they have put thesoftware which runs those difficult calculations into their website's Javascript. This then causes the computers belonging to the visitors of their website to run those calculations for them, instead ofrunning them themselves. In other words, when you visit a website with an embedded crypto-miner in it, your computer and electricity is used to try to generate crypto-coins for the owners of thatwebsite. Although there are various measures being applied to stop these illegitimate minings, the trend is still increasing. This research aims to find out potential gaps in current methodologies anddevelop a solution that can fulfil the gap. It also aims to find out:• What type crypto mining methodologies are being applied?• Apart from crypto-mining, what other security risks may it introduce? For example: cryptojacking• How current web standards are tackling this problem?"
thesis4.superviser ='Sami Azam'

thesis5 = thesis_projects()
thesis5.topic_num = 176
thesis5.title = 'Artificial Intelligence in Health Informatics'
thesis5.description ='The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithm. The findings will be analysed and compared to similar research works.'
thesis5.superviser ='Asif Karim'


thesis6 = thesis_projects()
thesis6.topic_num = 180
thesis6.title = 'Unsupervised Model Development from Autism Screening Data '
thesis6.description ='The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests. '
thesis6.superviser ='Asif Karim'


thesis7 = thesis_projects()
thesis7.topic_num = 226
thesis7.title = 'Applying Artificial Intelligence to solve real world problems'
thesis7.description ='Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.'
thesis7.superviser ='Bharanidharan Shanmugam'



projects = [thesis1, thesis2, thesis3, thesis4, thesis5, thesis6, thesis7]

"""


def home(request):
    return render(request, 'as2_app/home.html')
def projectlist(request):

    thesis1 = thesis_projects()
    thesis1.topic_num = 1
    thesis1.title = 'Machine learning approaches for Cyber Security'
    thesis1.description = 'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction andfor an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.'
    thesis1.superviser = 'Bharanidharan Shanmugam'
    
    
    thesis2 = thesis_projects()
    thesis2.topic_num = 9
    thesis2.title = 'Informetrics applications in multidisciplinary domain'
    thesis2.description = 'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniqueson various information artefact have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary researchliterature using various machine learning, network analysis, data visualisation and data wrangling tools.'
    thesis2.superviser = 'Yakub Sebastian'
    
    
    thesis3 = thesis_projects()
    thesis3.topic_num = 16
    thesis3.title = 'Development of a Virtual Reality System to Test Binaural Hearing'
    thesis3.description ='A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design,implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.'
    thesis3.superviser ='Sami Azam'
    
    
    thesis4 = thesis_projects()
    thesis4.topic_num = 41
    thesis4.title = 'Current trends on cryptomining and its potential impact on cryptocurrencies'
    thesis4.description ="Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computersand spend a lot of time and money running them to perform the difficult calculations to generate crypto coins. Some website owners have started taking a different approach; they have put thesoftware which runs those difficult calculations into their website's Javascript. This then causes the computers belonging to the visitors of their website to run those calculations for them, instead ofrunning them themselves. In other words, when you visit a website with an embedded crypto-miner in it, your computer and electricity is used to try to generate crypto-coins for the owners of thatwebsite. Although there are various measures being applied to stop these illegitimate minings, the trend is still increasing. This research aims to find out potential gaps in current methodologies anddevelop a solution that can fulfil the gap. It also aims to find out:• What type crypto mining methodologies are being applied?• Apart from crypto-mining, what other security risks may it introduce? For example: cryptojacking• How current web standards are tackling this problem?"
    thesis4.superviser ='Sami Azam'
    
    thesis5 = thesis_projects()
    thesis5.topic_num = 176
    thesis5.title = 'Artificial Intelligence in Health Informatics'
    thesis5.description ='The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithm. The findings will be analysed and compared to similar research works.'
    thesis5.superviser ='Asif Karim'
    
    
    thesis6 = thesis_projects()
    thesis6.topic_num = 180
    thesis6.title = 'Unsupervised Model Development from Autism Screening Data '
    thesis6.description ='The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests. '
    thesis6.superviser ='Asif Karim'
    
    
    thesis7 = thesis_projects()
    thesis7.topic_num = 226
    thesis7.title = 'Applying Artificial Intelligence to solve real world problems'
    thesis7.description ='Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.'
    thesis7.superviser ='Bharanidharan Shanmugam'
    
    
    
    projects = [thesis1, thesis2, thesis3, thesis4, thesis5, thesis6, thesis7]

    
    return render(request, 'as2_app/projectlist.html', {'projects': projects})

def about(request):
    return render(request, 'as2_app/about.html')

def project_details(request, projects):
    pass
 