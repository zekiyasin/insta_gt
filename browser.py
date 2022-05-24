from selenium import webdriver
import kullanıcı as kb
import time
from selenium.webdriver.chrome.options import Options

class Browser:
	def __init__(self,link):
		self.link = link
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
  
		self.browser = webdriver.Chrome("./chromedriver.exe",chrome_options=chrome_options)
		self.userName = kb.userName
		self.password = kb.password
		Browser.goInstagram(self)

	def goInstagram(self):
		self.browser.get(self.link)
		time.sleep(2)
		Browser.login(self)

		takipçiler = Browser.getFollowers(self)
		takipler = Browser.get_takip(self)
		Browser.compare(self,takipçiler,takipler)

	def getFollowers(self):
		self.browser.find_element_by_xpath('//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a').click()
		time.sleep(4)

		Browser.scrollDown(self)
		time.sleep(2)

		takipciler = self.browser.find_elements_by_css_selector(".notranslate._0imsa") 
		sayac = 0
		takipçiler = []
		for takipci in takipciler:
			sayac += 1
			print(str(sayac) + " --> " +takipci.text)
			takipçiler.append(takipci.text)

		sayac = 0
		f = open("followers.txt","w")
		for i in takipçiler:
			sayac += 1
			f.write(f"{sayac} --> {i}\n")
			
		return takipçiler
   
   
	def get_takip(self,):
		self.browser.get(self.link+"/"+kb.userName)
		time.sleep(5)
		self.browser.find_element_by_xpath('//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a').click()
		time.sleep(4)
		Browser.scrollDown(self)
		time.sleep(2)
		takip_edilenler = self.browser.find_elements_by_css_selector(".notranslate._0imsa")
		takipler = []
		sayac = 0
		for takip in takip_edilenler:
			sayac += 1
			print(str(sayac) + " --> " +takip.text)
			takipler.append(takip.text)

		sayac = 0
		f = open("follows.txt","w")
		for i in takipler:
			sayac += 1
			f.write(f"{sayac} --> {i}\n")
		return takipler

	def compare(self,takipçiler,takipler):
		fenomenler =  ['ankaderresmi', 'birlikteskilati', 'gurbeyahmedov', 'annelersatiyorcom', 'av.dr.aslanabiduguz_karate', 'leilapolak', 'pendikitosaaihl', 'gtuedutr', 'bitcicom', 'bitcicomglobal', 'evrimshinka', 'karate_turk', 'yasiryilmaz0', 'kaanbosnakofficial', 'unlostv', 'skamaroshek', 'rnfkk_kyokushin_official', 'rraenee', 'kyokushinspirit', 'superkarate', 'tugkangonultas', 'tburaksahin', 'tolgaozuygur', 'ismetozeltr', 'gencliksporbak', 'enesbatur', 'kendinemuzisyen', 'yuzyuzeykenkonusuruz', 'delimine', 'formulaonereels', 'eftalyayagcii', 'barisozcan', 'cembolukbasi', 'fatihyasinim', 'atakanozyurt', 'berkcan', '1kyokushin', 'yuzyuzeykens', 'yeniikinciler', 'rterdogan', 'ekremimamoglu', 'firatalbayram', 'webtekno', 'bilalhanci', 'f1', 'charles_leclerc', 'ceydakasabali', 'landonorris', 'egefitness']
		f = open("gt.txt","w")
		not_follower = []
		for i in takipler:
			if i in takipçiler:
				continue
			else:
				if i in fenomenler:
					continue
				else:
					not_follower.append(i)

		print("geri takip etmeyenler: ")
		sayac = 0
		for i in not_follower:
			sayac += 1
			print(f"{sayac} --> {i}")
			f.write(f"{sayac} --> {i}\n")
		

	def scrollDown(self):
		jsKomut = """
		sayfa = document.querySelector(".isgrP");
		sayfa.scrollTo(0,sayfa.scrollHeight);
		var sayfaSonu = sayfa.scrollHeight;
		return sayfaSonu;
		"""
		sayfaSonu = self.browser.execute_script(jsKomut)
		while True:
			son = sayfaSonu 
			time.sleep(1)
			sayfaSonu = self.browser.execute_script(jsKomut)
			if son == sayfaSonu:
				break


	def login(self):
		username = self.browser.find_element_by_name("username")
		password = self.browser.find_element_by_name("password")

		username.send_keys(kb.userName)
		password.send_keys(kb.password)

		loginBtn = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
		loginBtn.click()
		# time.sleep(4)
  
		# verification_code = input("Enter verification code: ")
  
		# time.sleep(60)
  
		# code = self.browser.find_element_by_name("verificationCode")
		# code.send_keys(verification_code)
  
		# verify_button = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[2]/button')
		# verify_button.click()
		time.sleep(10)
  
		self.browser.execute_script(f'''window.open("{self.link+"/"+kb.userName}");''')
		self.browser.switch_to.window(self.browser.window_handles[1])
		time.sleep(3)