from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .services import *
from django.core.cache import cache
from django.conf import settings

def index(request):
    if 'USER_ID' not in request.session:
        request.session['USER_ID'] = get_random_string(20)
    context = {
    }
    return render(request, 'AMTSurvey/index.html', context)

def pre_survey_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/pre_survey.html', context)

def save_pre_survey(request):
    q1 = request.POST.get("q1", "")
    q2 = request.POST.get("q2", "")
    q3 = request.POST.get("q3", "")

    # save q1, q2, q3
    save_pre_survey_data(request,q1,q2,q3)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_1') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_view(request):
    context = {
    }
    # book_list = get_books_mental_model(request)
    # print(book_list)
    book_list = {0: {'isbn': '1855327791', 'title': 'Typhoon and Tempest Aces of World War 2 (Osprey Aircraft of the Aces No 27)', 'description': 'Osprey\'s Aircraft of the Aces series combines full colour artwork, the best archival contemporary photography, and first hand accounts from aces to bring history\'s greatest airborne conflicts to life."', 'image_url': 'http://books.google.com/books/content?id=gPRZvgAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 1: {'isbn': '0385739915', 'title': 'Never Ending', 'description': 'Gr 9 Up—Shiv is embarking on a somewhat experimental therapeutic treatment to help her recover from the sudden death of her younger brother, Declan, during a family vacation in Greece. Shiv\'s story shifts back and forth in time so that readers are gradually informed about the tensions that emerged on that fateful vacation, the competition Shiv and Declan felt for the attentions of glamorous Nikos, their guide on a scuba diving expedition, and the lies Shiv told to maintain her relationship with Nikos while excluding Declan. No wonder she feels guilty. But she\'s not alone. Each of the young adults at the Korsakoff Clinic has suffered the traumatic loss of a loved one and each of them feels responsibility for the death. At first, the course of therapy seems relatively benign: walking, talking, and writing. The subsequent stages are much more brutal and are intended to break the patients psychologically in order to patch them together again. This is a dangerous process, and not all of the teens will be able to recover their equilibrium. Part-mystery, part-romance, and part-disturbing portrait of how fragile the human psyche can be, this novel is provocative and not for the faint of heart.—Miriam Lang Budin, Chappaqua Library, NY"', 'image_url': 'default'}, 2: {'isbn': '0674604814', 'title': 'The Nature of the Common Law', 'description': "This is a first-rate study of the principles that govern decision-making under common law--it brings out how the social functions of the courts bear on the correctness of a decision. Unlike many works on this topic, it is rich in examples, and sensitive to actual judicial practice. (Judith Jarvis ThomsonMassachusetts Institute of Technology)Professor Eisenberg has written a concise, thoughtful and refreshingly optimistic account of the common law tradition. (Harry H. WellingtonYale Law School)'", 'image_url': 'http://books.google.com/books/content?id=xpsJtgBYdroC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api'}, 3: {'isbn': '155725463X', 'title': "You Converted Me: The Confessions of St. Augustine (Classics of Christian Faith for Today's Readers)", 'description': 'Tony Jones (M.Div., Ph.D.) is a theologian, professor, and writer. Currently, he serves as theologian-in-residence at Solomon\'s Porch in Minneapolis, and teaches in the doctor of ministry program at Fuller Theologian Seminary. Tony has written ten books on Christian ministry, spirituality, prayer, and new church movements."', 'image_url': 'http://books.google.com/books/content?id=SSQ4Mrqe8ZsC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api'}, 4: {'isbn': '159998055X', 'title': 'The Gripping Beast', 'description': "Charlene Teglia is the award-winning author of seventeen novels and novellas in a variety of erotic romance subgenres. She lives in Washington with her husband and two daughters. Visit her website at www.charleneteglia.com.'", 'image_url': 'http://books.google.com/books/content?id=GgSEswEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 5: {'isbn': '0761366350', 'title': "Delicious Vegetarian Main Dishes (You're the Chef)", 'description': 'Gr 1-4-These recipes manage to hit a sweet spot in kid cookery: they require little in the way of expertise, yet are complex enough to be interesting. None of your "Ants on a Log" nonsense here. Young chefs will be taking a stab at "Tasty Pad Thai Noodles," "Chicken Wonton Soup," and "Terrific Turkey Burgers." The instructions are detailed and thoroughly illustrated with clear color drawings; photos show the enticing final products. The ingredients are readily available and include very few processed foods and only one or two convenience items-after all who could blame cooks for buying a bag of shredded carrots instead of julienning two cups of carrots themselves? The 9 or 10 recipes in each book focus on nutritious ingredients but aren\\\'t stingy with the cheese. Most of them have a suggested "Try This!" variation that gently encourages kids to get creative with their cooking. α(c) Copyright 2011.  Library Journals LLC, a wholly owned subsidiary of Media Source, Inc.  No redistribution permitted.\'', 'image_url': 'default'}, 6: {'isbn': '0399526137', 'title': 'Triumphs of the Heart: Miraculous True Stories of the Power of Love', 'description': 'Chris Benguhe, who became a writer to help make the world a better place, celebrates "the most important things in life... people and the support and love we give each other" in Triumphs of the Heart: Miraculous True Stories of the Power of Love, with an introduction by George W. Bush. Though presented with forced drama, many of these 25 tales of real people\\\'s heroism, compassion and generosity are hopeful and inspiring. Agents, Becker & Mayer. (Berkley/Perigee, $12 paper 208p ISBN 0-399-52613-7; Aug.)Copyright 2000 Cahners Business Information, Inc.\'', 'image_url': 'http://books.google.com/books/content?id=VrxL7dWbY70C&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 7: {'isbn': '0609803026', 'title': 'Basic Japanese Coursebook: Revised and Updated (LL(R) Complete Basic Courses)', 'description': 'Learn step-by-step in 40 easy lessonsGrammar & Usage Explained ThroughoutComprehensive reference sections IncludedFor Beginners or Those Who Want a Thorough ReviewLearn to speak, read, and write Japanese quickly and easily withLiving Language. Developed by U.S. government experts, this book introduces you step-by-step to the basics of Japanese pronunciation, vocabulary, idiomatic expressions, and grammar.Inside You\'ll Find:All the words and phrases from the 40 lessons on theLiving LanguageJapanese Complete Courserecordings plus additional vocabularyA guide to pronunciationUseful topics: Directions, Introductions, Shopping, etc.Explanations of grammar and usageShort quizzes to help you check your progressA comprehensive summary of Japanese grammarVerb charts, including all tensesA special section on writing lettersWhile this book stands on its own as an instructional program and an invaluable reference, you\'ll find that using it with the recorded lessons is even more effective. Along with the recordings,Living LanguageJapanese Complete Coursecassette and compact disc packages include this book as well as a dictionary."', 'image_url': 'http://books.google.com/books/content?id=iD5XNwAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 8: {'isbn': '0202020339', 'title': 'Human Biodiversity: Genes, Race, and History (Foundations of Human Behavior)', 'description': "“Outstanding Title!... Marks traces the history of scientific attempts to describe and account for human biological variation. Covering the 17th century to the present, his study stresses the derivation of scientific ideas from the social problems and values with which they share history… A highly readable, thought-provoking, and comprehensive treatment of popular and scholarly interest in race and human variation. General readers; upper-division undergraduates and above.”—S. A. Quandt,Choice“[Jonathan Marks’s] thoughtful and witty book is about one of the “wrongest” of scientific notions: namely, the idea that the human species can be divided into discrete biological subunits, or races…. Marks casts his book as both an introduction to the current state of human genetics and a cautionary historical tale about what happens when scientists do not examine their most basic assumptions. Beginning in 1699 with the publication of Edward Tyson’s famous comparison of a human and a chimp, Marks structures his historical account around the assumptions that have given rise to the 20th-century biological concept of race…. What Marks has given us is truly a “people’s history of human biodiversity.” I do not know of a more lively and heartfelt introduction.”—Misia Landau,American Anthropologist'", 'image_url': 'http://books.google.com/books/content?id=zlvknQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 9: {'isbn': '1433803372', 'title': 'Cultural Competence in Trauma Therapy: Beyond the Flashback', 'description': 'Laura S. Brownreceived a Ph.D. in Clinical Psychology in 1977 from Southern Illinois University at Carbondale, and has been in practice as a clinician and forensic psychologist in Seattle since 1979. She has served on the faculties of Southern Illinois University, U. of Washington, and the Washington School of Professional Psychology. A Diplomate in Clinical Psychology and a Fellow of ten APA divisions, Dr. Brown\'s work in the fields of feminist therapy theory and trauma treatment has received numerous awards from her peers, including the Distinguished Publications Award of the Association for Women in Psychology, APA\'s Award for Distinguished Professional Contributions to Public Service, the Sarah Haley Award for Clinical Excellence from ISTSS, and the Carolyn Wood Sherif Award from the Society for the Psychology of Women. She is the therapist featured in two videos on trauma treatment in the APA Video Series, and is a founding member of the Division of Trauma Psychology of APA."', 'image_url': 'http://books.google.com/books/content?id=_eRrAAAAMAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 10: {'isbn': '0312420994', 'title': 'The Zig Zag Kid', 'description': "Noted for both his provocative journalism (e.g., The Yellow Wind, LJ 4/15/88) and his fiction (e.g., The Book of Common Grammar, LJ 4/15/94), Israeli writer Grossman here offers an imaginative new tale whereby the rebellious son of a detective is whisked away by a friendly kidnapper on the trail of the trademark purple scarf of actress Lola Ciperola.Copyright 1997 Reed Business Information, Inc.--This text refers to an out of print or unavailable edition of this title.'", 'image_url': 'http://books.google.com/books/content?id=7_601G2OqN4C&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api'}, 11: {'isbn': '1416957901', 'title': "Click!: The Girl's Guide to Knowing What You Want and Making It Happen", 'description': 'Annabel (Schwedes) Monaghanspent her teenage yearsalmostmaking it happen. Annabel\'s claim to fame is being dumped by the cutest guyin Los Angeles--twice! She had dinner with Madonna once. Okay, not at thesame table, but at the same restaurant. A former investment banker, she\'smuch happier writing.Elisabeth (Koller) Wolfewas the only cheerleader in Richmond, Virginiato be kicked off the squad for chronic lateness due to humidity hair havoc.Thankfully, Elisabeth refocused her energy and moved to New York City, whereshe became an attorney, started a production company, and won an Emmy Award."', 'image_url': 'http://books.google.com/books/content?id=5dIaZZ6uS0wC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api'}, 12: {'isbn': '1441535136', 'title': 'From The Outside In And Back Again: A Falingsdale Tale', 'description': 'In 1975 J.M.A. Quinn was born Joseph Michael Arlo Quinn in Sayre Pennsylvania. From a young age he was drawn to art which furthered his curiosity into music and writing. An avid blogger and an author of published poetry. Music is often an underlying inspiration for many of his works. Please check out J.M.A Quinn\'s website at www.JMAQUINN.com"', 'image_url': 'http://books.google.com/books/content?id=z3bywAEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 13: {'isbn': '0736648631', 'title': 'Why They Kill', 'description': 'The normally pedantic Richard Rhodes presents a loosely disguised biography of Lonnie Athens, a fringe criminologist shunned by his peers, who spent 10 years interviewing violent humans in prisons. When a sociology journal editor read Athens\\\'s doctoral thesis, he claimed it was the worst article he had ever been sent to review, calling it a "mysterious analysis of stream of consciousness." The narrator\\\'s cheery drone of Athens\\\'s loosely defined terms (for example, "violentization," "frustrated malifaction," and "incipient violent self-image") breaks the cadence into petulant, guttural lingo as inmates recount their thoughts during a rape. The horrific tales stand as islands in a sea of words.  J.A.H. © AudioFile 2001, Portland, Maine--Copyright © AudioFile, Portland, Maine\'', 'image_url': 'default'}, 14: {'isbn': '1439240906', 'title': 'My Brain Gets Full', 'description': "G. Gayle Kelley lives in a small central Kentucky town, Carlisle, with his wife Donna and grandson Jon.  His educational/work background is business management.  In the late nineties, he added two years of computer-related studies to his educational background and entered the technology world, focusing on business processes and procedures.  He suffered a traumatic brain injury while working as the Business Transformation Manager for a procurement and distribution center in Cincinnati, Ohio, in 2002.  You can visit his estore at https://www.createspace.com/1000250450  or his website http://www.ggaylekelley.com.'", 'image_url': 'default'}, 15: {'isbn': '0062109391', 'title': 'This Will Make You Smarter: New Scientific Concepts to Improve Your Thinking', 'description': "“This Will Make You Smartergives us better tools to think about the world and is eminently practical for life day to day. The people in this book lead some of the hottest fields.” (DAVID BROOKS, from the Foreword)“The world’s smartest website ... Edge is a salon for the world’s finest minds” (The Guardian)“Edge.org has become an epicenter of bleeding-edge insight across science, technology and beyond, hosting conversations with some of our era’s greatest thinkers” (Atlantic Monthly)“A winning combination of good writers, good science and serious broader concerns.” (KIRKUS REVIEWS (starred review))'", 'image_url': 'http://books.google.com/books/content?id=v0idZwEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 16: {'isbn': '142515400X', 'title': 'Blue Star: Fulfilling Prophecy', 'description': 'Miriam Delicado, author of \'Blue Star, is a middle-aged woman that has always had an array of abilities and sensitivities. She is able to heal, predict earthquakes, connect with crossed-over spirits and astral travel. She also has psychic ability and gets premonitions. Her first memory is of being a baby and feeling the frustration of not being able to communicate with others. Her life story encompasses much that is strange. She was first contacted by Aliens while a baby and was abducted for the first time at age four. These particular events were not in her consciousness until much later in her life. The trigger that brought these occurrences back into her consciousness was an Alien abduction experience while on a road trip in 1988. Her journey leads her to The Four Corners Area of the southwestern United States. Since that time there have been many other encounters with \'Tall Blond\' Aliens. The relationship that developed between Miriam and the Aliens became one of Teacher-Student and finally culminated into that of Emissary. As a direct request from the \'Tall Blonds\', and to fulfill the role of Emissary, she has written \'Blue Star - Fulfilling Prophecy\'. In this book Miriam recounts her experiences with the Aliens, her travels to the Alien \'Safe Lands\', her meetings with Hopi elders and the connections with indigenous peoples prophecies. She also shares the Alien\'s history of Man\'s creation and their involvement with Earth and \'The End Times\'.--This text refers to thePaperbackedition."', 'image_url': 'http://books.google.com/books/content?id=aM1aPQAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 17: {'isbn': '0273719238', 'title': 'Advanced Modern Engineering Mathematics (4th Edition)', 'description': "Advanced Modern Engineering MathematicsGlyn Jamesfourth\xa0editionBuilding on the foundations laid in the companion textModern Engineering Mathematics, this book gives an extensive treatment of some of the advanced areas of mathematics that have applications in various fields of engineering, particularly as tools for computer-based system modelling, analysis and design.Despite the advanced level of this text, the philosophy of learning by doing is retained, with continuing\xa0emphasis on\xa0the development of students\x92 ability to use mathematics with understanding to solve engineering problems.Key features of this new edition:·\xa0\xa0\xa0\xa0\xa0\xa0\xa0 The order of chapters is updated, giving a more logical progression throughout the book·\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Colour is introduced to make the text more accessible and student-friendly·\xa0\xa0\xa0\xa0\xa0\xa0\xa0 More references are made to the use of MATLAB and MAPLE with commands and codes introduced·\xa0\xa0\xa0\xa0\xa0\xa0\xa0 New topics are introduced, including new sections on singular value decomposition, direct design of digital filters and windows, and integral solution of partial differential equations·\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Updated Solutions Manual; a downloadable resource for lecturersProfessorGlyn Jamesis currently Emeritus Professor in Mathematics at Coventry University, having previously been Dean of the School of Mathematical and Information Sciences. As in previous editions he has drawn on the relevant knowledge and experience of his fellow co-authors to provide an excellent new edition.\xa0'", 'image_url': 'http://books.google.com/books/content?id=iwzBbwAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}, 18: {'isbn': '1596910712', 'title': 'The Naming of Names: The Search for Order in the World of Plants', 'description': 'Pavord, author of the The Tulip and an expert gardener, traces the history of plant taxonomy from the ancient Greeks to 17th-century British botanist John Ray in this hefty tome, and though her passion for plants is apparent on every page, readers who don\\\'t share the same level of enthusiasm will be frustrated by Pavord\\\'s encyclopedic approach. Pavord, in prose as rich and colorful as the too-infrequent illustrations, contextualizes plant classification within larger intellectual, political and cultural spheres, but she verges dangerously close to writing a textbook; the vast amount of information she packs into brief, rapid-fire sections can overwhelm. In the best sections, she slows down to draw detailed portraits of researchers and describe how each contributed to the slowly evolving (and, until the late 1600\\\'s, unnamed) science of botany. Ray, for instance, marked "a quiet, lonely, dogged consummation" with "no fireworks, no claps of thunder, no swelling symphonic themes" when, shortly before his death and suffering from gangrene, he penned the six fundamental rules of botany. Pavord\\\'s prose dazzles, but it\\\'s not enough to carry readers with a casual interest in plants or gardening through an otherwise dense history.Copyright © Reed Business Information, a division of Reed Elsevier Inc. All rights reserved.\'', 'image_url': 'default'}, 19: {'isbn': '0688105696', 'title': 'Slow Dance Heart Break Blues', 'description': 'Grade 7-10?Playing with shape and rhythm is nothing new for Adoff, and here he uses those techniques to illuminate the thoughts of adolescents. Words fall on the pages as images might come and go from a teen\\\'s mind and mouth. From the very brief (one poem is only four words long) to the full-page barrage of emotions, the poet is quite adept at listening to the voices in readers\\\' heads. "Will I ever learn to love me first?" and "Will the sun for real rise up tomorrow?" are just two of the alternately philosophical and realistic concerns just bursting to be released from the jumble of the teenage mind. Adoff uncovers the masks teens wear, poses the question of love versus lust, offers a look at the dangers of drug use, and presents telling glimpses of body image. There is a beat to many of the selections, keeping readers moving forward. The poems\\\' free-form shapes enforce the transitory and flashing images. In one sense, the structure aids the readability, making the verses appear as quick reads. But there is a great deal of depth here, with some of the selections providing more of an intellectual challenge. These flashes are fast and funky and will have readers questioning not only what poetry is (and isn\\\'t), but also taking another look at who and where they are in light of today\\\'s fast-moving issues and society.?Sharon Korbeck, formerly at Milwaukee Public LibraryCopyright 1995 Reed Business Information, Inc.\'', 'image_url': 'http://books.google.com/books/content?id=REvhAAAAMAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'}}
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model.html', context)

def save_mental_model(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result)
    response = { 'status' : 1 , 'redirect-url' : reverse('part_3_directions') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def part_3_directions_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/part_3_directions.html', context)

def session_1_view(request):
    context = {
    }
    # handle error if familiar and interest are empty
    familiar_list = get_familiar_cluster(request)
    interest_list = get_interest_cluster(request)
    if settings.MODE_FLAG == 0:
        book_list = get_familiar_book(request, familiar_list)
    else:
        book_list = get_interest_book(request, interest_list)

    context['books'] = book_list
    return render(request, 'AMTSurvey/session_1.html', context)

def session_2_view(request):
    context = {}
    # handle error if familiar and interest are empty
    familiar_list = get_familiar_cluster(request)
    interest_list = get_interest_cluster(request)

    if settings.MODE_FLAG == 0:
        book_list = get_interest_book(request, interest_list)
    else:
        book_list = get_familiar_book(request, familiar_list)

    context['books'] = book_list
    return render(request, 'AMTSurvey/session_2.html', context)

def post_survey_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/post_survey.html', context)

def thank_you_view(request):
    context = {
        'user_id' : request.session.get('USER_ID')
    }
    del request.session['USER_ID']
    return render(request, 'AMTSurvey/thank_you.html', context)

def save_session_1(request):
    result = request.POST.get("response" , '')
    save_curiosity_session(request, result, 1)
    response = { 'status' : 1 , 'redirect-url' : reverse('session_2') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def save_session_2(request):
    result = request.POST.get("response" , '')
    save_curiosity_session(request, result, 2)
    response = { 'status' : 1 , 'redirect-url' : reverse('post_survey') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def save_post_survey(request):
    q1 = request.POST.get("q1", "")
    q2 = request.POST.get("q2", "")
    q3 = request.POST.get("q3", "")

    # save q1, q2, q3
    save_post_survey_data(request,q1,q2,q3)
    response = { 'status' : 1 , 'redirect-url' : reverse('thank_you') }

    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_1_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 1)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_1.html', context)

def save_mental_model_1(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 1)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_2') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_2_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 2)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_2.html', context)

def save_mental_model_2(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 2)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_3') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_3_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 3)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_3.html', context)

def save_mental_model_3(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 3)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_4') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_4_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 4)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_4.html', context)

def save_mental_model_4(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 4)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_5') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_5_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 5)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_5.html', context)

def save_mental_model_5(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 5)
    response = { 'status' : 1 , 'redirect-url' : reverse('part_3_directions') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def get_book_details(request):
    isbn = request.POST.get("ISBN", '')
    books_dict = pickle.load(default_storage.open('./data/pickles/books_space_dict.pkl', mode='rb'))
    book = books_dict[isbn]

    response = { 'status' : 1 , 'book_details' : book }
    return render(request, 'AMTSurvey/includes/book_detail_modal.html', {'title' : book['title'], 'desc': book['desc'] , 'image_url': book['image_url']})
    # return HttpResponse(json.dumps(response), content_type="application/json")

