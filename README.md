
<center>
<h1><a href="https://mhw-encyclopedia.herokuapp.com/">MHW-Encyclopedia</a><h1>
<img src='https://res.cloudinary.com/di8ugfihk/image/upload/v1684003006/diablos_info_ie73od.jpg'></img>

<hr>

<h4>Description</h4>
Learn about etymology and the lifestyles of creatures that exist within the vast Monster Hunter World, and dive into the ecosystems that support the unique lifeforms which draw inspiration from ours and fantasy.
    <br></br>
<p>MHW (Monster Hunter World) Encyclopedia is a website that holds a collection of monsters large and small from the game Monster Hunter World released by Capcom in 2018. This application was built upon the technologies of Django and Python utilizing Postgresql as it's database, and aims to be a stylish academic-inspired alternative to wikis where players and non-players alike can educate themselves on the monsters and environments. 
<br></br>
Within the encyclopedia you will also find exclusive information about the monster's ecology, habits, and hierachical structures visualized by food chains. You can find articles that meticulously peruse over all the history and known studies about the places these monsters inhabit and how they came to be. 
<br></br>
As a user you'll be able to register as a Hunter and gain access to your own personal material gathering list to help you stay organized when playing through the game and micro-managing materials, as well as view what weaknesses a monster might have to certain attributes and situations. 
<br></br>
Built & Designed By <a href='https://www.linkedin.com/in/erichungdev/'>Eric Hung</a>.    
View the app <a href='https://mhw-encyclopedia.herokuapp.com/'>HERE</a>.    
</p>

<br>
<h4>Resources & Links</h4>
<hr>
<p>View the user stories, items implemented, and future upcoming enhancements all in the Trello Board <a href='https://trello.com/invite/b/95K0Zy1U/ATTI29d0c6de97d1199fcddd9b843edba1b79158B0A2/mhw-encyclopedia'>HERE.</a></p>

<p>View the original wireframes, design roots, and ERD diagrams within the Whimsical link provided <a href='https://whimsical.com/mhw-encyclopedia-wire-erd-7Aiq3F9Z3fptTmu9gvi9Fn'>HERE.</a></p>

<br>
<h4>Technologies Used</h4>

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

<hr>
<br>
<h4>The Application & More</h4>
<br>
<img src='https://res.cloudinary.com/di8ugfihk/image/upload/v1684035863/Screenshot_2023-05-13_at_8.43.39_PM_yob1bh.png'>
<br></br>
<p>Monsters will be available to view by category and within a carousel format that displays an image of the monster alongside it's name and description. Note that the information displayed on the website was gathered from the MHW API which is not fully up to date with the most recent releases and updates made to the game, thus some of the discrepancy you might notice if you have played through the full contents of the game.</p>
<br>
<h4>User Functionality</h4>
<br>
<img src='https://res.cloudinary.com/di8ugfihk/image/upload/v1684040472/Screenshot_2023-05-13_at_10.00.51_PM_fhxnph.png'>
<br></br>
<p>Once logged in as a registered user this is the view where you will be able to customize your material list and manage them depending on the status of the materials. This is intended to be used by players who are active in the game to allow for real-time material management in sync with the game's wishlist system which is not built out for full on customizability.</p>
<br>
<h4>Search Functionality</h4>
<br>
<img src='https://res.cloudinary.com/di8ugfihk/image/upload/v1684117340/Screenshot_2023-05-14_at_7.20.28_PM_uothez.png'>
<br></br>
<p>The searchbar allows users to search through the database for any monsters regardless of type, through their name field non-case sensitive. The results are clickable links that will direct the user towards that particular monster's detail page.</p>
<br>
<h4>Ecosystems & Articles</h4>
<br>
<img src='https://res.cloudinary.com/di8ugfihk/image/upload/v1684040841/Screenshot_2023-05-13_at_10.07.05_PM_yvyznu.png'>
<br></br>
<p>Information about each ecosystem is available organized under the following categories of descriptions, unique areas, local monster food-chains, harvestable materials, hazards, hunter notes, and additional snippets of relevant monster information.</p>
<hr>

<h4>Code Snippets</h4>
</center>
    
    def monster_detail(request, monster_name):
    url = f'https://mhw-db.com/monsters?q={{"name":"{monster_name}"}}'
    monster = requests.get(url).json()[0]
    monster_images = Monster_Image.objects.all()
    return render(request, 'monster_detail.html', {'monster': monster, 'monster_images':monster_images})

MHW-API and querying for monsters: This is one of the fetches using the url from the MHW-API database and the monster_name field from my monster_image model to match the correct image from my own database to the monster listed in the API.

    def home(request):
    all_monsters=requests.get('https://mhw-db.com/monsters').json()
    return render(request, 'home.html', {'all_monsters': all_monsters})

Here's an example of how to use the django shortcut 'requests' slightly different from the standard parameter request in order to fetch the entire monster database.

     {% for monster in large_monsters %}
        {% for mon in monster_images %}
            {% if monster.name == mon.name %}
        <div class="carousel-item">
            <a href="{% url 'monster_detail' monster.name %}">
            <img src="{{mon.image}}" class="d-block mx-auto" alt="..." style="height:45rem">
            <div class="carousel-caption d-none d-md-block">
            <h5>{{ monster.name }}</h5>
            <p>{{ monster.description }}</p>
            </div>
            </a>
        </div>
            {% endif %}
        {% endfor %}
      {% endfor %}

The above is the code used to implement the carousel design on the large monsters page by utilizing both the fetched API database in tandem with the built in monster_images database to match the right image asset to monster, both using a name field. 

<hr>
<h4>Future Enhancements</h4>
<br>
<ul>
<li><p>Adding Mobile Responsive Design</p></li>
<li><p>Adding Dropdown functionality on the navbar</p></li>
<li><p>Adding a Design-about page detailing color palettes and database structures</p></li>
<li><p>Updating the database to include most up to date monsters including the newest expansion</p></li>
<li><p>Adding the weapon library into the database and displaying them</p></li>
<li><p>Adding the materials and items library into the database and displaying them</p></li>
</ul>
