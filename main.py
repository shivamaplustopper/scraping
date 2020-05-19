import requests
import bs4
import csv

# banks will come #
res = requests.get('https://banksifsccode.com/all-banks.php')

soup = bs4.BeautifulSoup(res.text,'lxml')
links = soup.select('.bLists a')
file = open("d:/banks.csv","w")
for link in links:
    banks = link.get('href')
    writer = csv.writer(file)
    writer.writerow(banks)
file.close()
   


# States will come#
banks = ['allahabad-bank-ifsc-code','axis-bank-ifsc-code','abhyudaya-co-op-bank-ltd-ifsc-code', 'abu-dhabi-commercial-bank-ifsc-code', 'aditya-birla-idea-payments-bank-ifsc-code', 'ahmednagar-merchants-co-op-bank-ifsc-code', 'airtel-payments-bank-ifsc-code', 'akola-district-central-co-operative-bank-ifsc-code', 'akola-janata-commercial-cooperative-bank-ifsc-code','almora-urban-co-operative-bank-ltd-ifsc-code', 'ambarnath-jaihind-coop-bank-ifsc-code', 'andhra-bank-ifsc-code', 'andhra-pradesh-grameena-vikas-bank-ifsc-code', 'andhra-pragathi-grameena-bank-ifsc-code', 'apna-sahakari-bank-ltd-ifsc-code', 'au-small-finance-bank-limited-ifsc-code', 'australia-and-new-zealand-banking-group-limited-ifsc-code', 'bandhan-bank-limited-ifsc-code', 'bank-internasional-indonesia-ifsc-code', 'bank-of-america-ifsc-code', 'bank-of-bahrain-and-kuwait-ifsc-code', 'bank-of-baroda-ifsc-code', 'bank-of-ceylon-ifsc-code', 'bank-of-india-ifsc-code', 'bank-of-maharashtra-ifsc-code', 'bank-of-tokyo-mitsubishi-ufj-ltd-ifsc-code', 'barclays-bank-plc-ifsc-code', 'bassein-catholic-co-op-bank-ltd-ifsc-code', 'bhagini-nivedita-sahakari-bank-ifsc-code', 'bharatiya-mahila-bank-limited-ifsc-code', 'bnp-paribas-ifsc-code', 'canara-bank-ifsc-code', 'capital-local-area-bank-ltd-ifsc-code', 'capital-small-finance-bank-ifsc-code', 'catholic-syrian-bank-ltd-ifsc-code', 'central-bank-of-india-ifsc-code', 'chinatrust-commercial-bank-ifsc-code', 'citibank-na-ifsc-code', 'citizencredit-co-operative-bank-ltd-ifsc-code', 'city-union-bank-ltd-ifsc-code', 'commonwealth-bank-of-australia-ifsc-code', 'corporation-bank-ifsc-code', 'credit-agricole-corp-n-invsmnt-bank-ifsc-code', 'credit-suisse-ag-ifsc-code', 'dbs-bank-ltd-ifsc-code', 'dcb-bank-limited-ifsc-code', 'dena-bank-ifsc-code', 'deogiri-nagari-sahakari-bank-ltd-aurangabad-ifsc-code', 'deutsche-bank-ag-ifsc-code', 'development-credit-bank-limited-ifsc-code', 'dhanlaxmi-bank-ltd-ifsc-code', 'dicgc-ifsc-code', 'dmk-jaoli-bank-ifsc-code', 'doha-bank-qsc-ifsc-code', 'dombivli-nagari-sahakari-bank-limited-ifsc-code', 'durgapur-steel-peoples-co-operative-bank-ifsc-code', 'emirates-nbd-india-ifsc-code', 'equitas-small-finance-bank-limited-ifsc-code', 'esaf-small-finance-bank-ifsc-code', 'export-import-bank-of-india-ifsc-code', 'fincare-small-finance-bank-ltd-ifsc-code', 'fino-payments-bank-ifsc-code', 'firstrand-bank-limited-ifsc-code', 'g-p-parsik-bank-ifsc-code', 'gurgaon-gramin-bank-ifsc-code', 'haryana-state-cooperative-bank-ifsc-code', 'hdfc-bank-ltd-ifsc-code', 'himachal-pradesh-state-cooperative-bank-ltd-ifsc-code', 'hsbc-ifsc-code', 'icici-bank-ltd-ifsc-code', 'idbi-bank-ltd-ifsc-code', 'idfc-bank-ifsc-code', 'idrbt-ifsc-code', 'idukki-district-co-operative-bank-ltd-ifsc-code', 'india-post-payment-bank-ifsc-code', 'indian-bank-ifsc-code', 'indian-overseas-bank-ifsc-code', 'indusind-bank-ltd-ifsc-code', 'industrial-and-commercial-bank-of-china-limited-ifsc-code', 'industrial-bank-of-korea-ifsc-code', 'ing-vysya-bank-ltd-ifsc-code', 'irinjalakuda-town-co-operative-bank-ltd-ifsc-code','jalgaon-janata-sahkari-bank-ltd-ifsc-code', 'jana-small-finance-bank-ifsc-code', 'janakalyan-sahakari-bank-ltd-ifsc-code', 'janaseva-sahakari-bank-borivli-limited-ifsc-code', 'janaseva-sahakari-bank-ltd-pune-ifsc-code', 'janata-sahakari-bank-ltd-(pune)-ifsc-code', 'jio-payments-bank-ifsc-code', 'jpmorgan-chase-bank-na-ifsc-code', 'kallappanna-awade-ich-janata-sahakari-bank-ifsc-code', 'kapole-co-op-bank-ifsc-code', 'karnataka-bank-ltd-ifsc-code', 'karnataka-vikas-grameena-bank-ifsc-code', 'karur-vysya-bank-ifsc-code', 'kaveri-grameena-bank-ifsc-code', 'keb-hana-bank-ifsc-code', 'kerala-gramin-bank-ifsc-code', 'kotak-mahindra-bank-ifsc-code', 'kozhikode-district-co-op-bank-ifsc-code', 'krung-thai-bank-pcl-ifsc-code', 'kurmanchal-nagar-sahkari-bank-ltd-ifsc-code', 'laxmi-vilas-bank-ifsc-code', 'mahanagar-co-op-bank-ltd-ifsc-code', 'maharashtra-gramin-bank-ifsc-code', 'maharashtra-state-co-operative-bank-ifsc-code', 'mahesh-sahakari-bank-ltd-pune-ifsc-code', 'mashreq-bank-psc-ifsc-code', 'mizuho-corporate-bank-ltd-ifsc-code', 'mumbai-district-central-co-operative-bank-ltd-ifsc-code', 'nagar-urban-co-operative-bank-ifsc-code', 'nagpur-nagrik-sahakari-bank-ltd-ifsc-code', 'national-australia-bank-limited-ifsc-code', 'national-bank-for-agriculture-and-rural-development-ifsc-code', 'national-bank-of-abu-dhabi-nbad-ifsc-code', 'new--india-co-operative--bank--ltd-ifsc-code', 'nkgsb-co-op-bank-ltd-ifsc-code', 'north-east-small-finance-bank-ifsc-code', 'north-malabar-gramin-bank-ifsc-code', 'nsdl-payments-bank-ifsc-code', 'nutan-nagarik-sahakari-bank-ltd-ifsc-code', 'oman-international-bank-saog-ifsc-code', 'oriental-bank-of-commerce-ifsc-code', 'parsik-janata-sahakari-bank-ltd-ifsc-code', 'paytm-payments-bank-ltd-ifsc-code', 'pragathi-krishna-gramin-bank-ifsc-code', 'prathama-bank-ifsc-code', 'prime-co-operative-bank-ltd-ifsc-code', 'punjab-and-maharashtra-co-op-bank-ltd-ifsc-code', 'punjab-and-sind-bank-ifsc-code', 'punjab-national-bank-ifsc-code', 'qatar-national-bank-saq-ifsc-code', 'rabobank-international-(ccrb)-ifsc-code', 'rajarambapu-sahakari-bank-ifsc-code', 'rajgurunagar-sahakari-bank-limited-ifsc-code', 'rajkot-nagarik-sahakari-bank-ltd-ifsc-code', 'rbi-pad-ahmedabad-ifsc-code', 'rbl-bank-limited-ifsc-code', 'reserve-bank-of-india-ifsc-code', 'sahebrao-deshmukh-cooperative-bank-limited-ifsc-code', 'samarth-sahakari-bank-ltd-ifsc-code', 'sber-bank-ifsc-code', 'shikshak-sahakari-bank-limited-ifsc-code', 'shinhan-bank-ifsc-code', 'shivalik-mercantile-co-operative-bank-ltd-ifsc-code', 'shri-chhatrapati-rajarshi-shahu-urban-co-op-bank-ltd-ifsc-code', 'shri-veershaiv-co-op-bank-ifsc-code', 'sir-m-visvesvaraya-co-operative-bank-ifsc-code', 'small-industries-development-bank-of-india-ifsc-code', 'societe-generale-ifsc-code', 'solapur-janata-sahakari-bank-limited-ifsc-code', 'south-indian-bank-ifsc-code', 'standard-chartered-bank-ifsc-code', 'state-bank-of-bikaner-and-jaipur-ifsc-code', 'state-bank-of-hyderabad-ifsc-code', 'state-bank-of-india-ifsc-code', 'state-bank-of-mauritius-ltd-ifsc-code', 'state-bank-of-mysore-ifsc-code', 'state-bank-of-patiala-ifsc-code', 'state-bank-of-travancore-ifsc-code', 'sumitomo-mitsui-banking-corporation-ifsc-code', 'surat-national-co-op-bank-ifsc-code', 'suryoday-small-finance-bank-ifsc-code', 'syndicate-bank-ifsc-code', 'tamilnad-mercantile-bank-ltd-ifsc-code', 'telangana-state-coop-apex-bank-ifsc-code', 'textile-traders-co-operative-bank-ltd-ifsc-code', 'thane-bharat-sahakari-bank-ltd-ifsc-code', 'the-a-p-mahesh-co-op-urban-bank-ltd-ifsc-code', 'the-ahmedabad-mercantile-co-operative-bank-ltd-ifsc-code', 'the-andhra-pradesh-state-coop-bank-ltd-ifsc-code', 'the-bank-of-nova-scotia-ifsc-code', 'the-baramati-sahakari-bank-ltd-ifsc-code', 'the-bharat-co-operative-bank-(mumbai)-ltd-ifsc-code', 'the-cosmos-co-operative-bank-ltd-ifsc-code', 'the-delhi-state-cooperative-bank-limited-ifsc-code', 'the-federal-bank-ltd-ifsc-code', 'the-gadchiroli-district-central-cooperative-bank-ltd-ifsc-code', 'the-greater-bombay-co-op-bank-ltd-ifsc-code', 'the-gujarat-state-co-operative-bank-ltd-ifsc-code', 'the-hasti-co-op-bank-ltd-ifsc-code', 'the-jalgaon-peoples-co-op-bank-ifsc-code', 'the-jammu-and-kashmir-bank-ltd-ifsc-code', 'the-kalupur-commercial-co-op-bank-ltd-ifsc-code', 'the-kalyan-janata-sahakari-bank-ltd-ifsc-code', 'the-kangra-central-co-op-bank-limited-kccb-ifsc-code', 'the-kangra-co-operative-bank-ltd-ifsc-code', 'the-karad-urban-co-op-bank-ltd-ifsc-code', 'the-karnataka-state-co-operative-apex-bank-ltd-ifsc-code', 'the-lakshmi-vilas-bank-ltd-ifsc-code', 'the-mehsana-urban-cooperative-bank-ltd-ifsc-code', 'the-municipal-co-operative-bank-ltd-mumbai-ifsc-code', 'the-nainital-bank-limited-ifsc-code', 'the-nasik-merchants-co-op-bank-ltd-nashik-ifsc-code', 'the-navnirman-co-operative-bank-limited-ifsc-code', 'the-pandharpur-urban-co-op-bank-ltd-ifsc-code', 'the-rajasthan-state-cooperative-bank-ltd-ifsc-code', 'the-ratnakar-bank-ltd-ifsc-code', 'the-royal-bank-of-scotland-nv-ifsc-code', 'the-saraswat-co-operative-bank-ltd-ifsc-code', 'the-seva-vikas-co-operative-bank-ltd-ifsc-code', 'the-shamrao-vithal-co-operative-bank-limited-ifsc-code', 'the-sindhudurg-district-central-coop-bank-ltd-ifsc-code', 'the-surat-district-co-operative-bank-ltd-ifsc-code', 'the-surat-peoples-co-op-bank-ltd-ifsc-code', 'the-sutex-co-op-bank-ltd-ifsc-code', 'the-tamilnadu-state-apex-cooperative-bank-limited-ifsc-code', 'the-thane-district-central-co-op-bank-ltd-ifsc-code', 'the-thane-janata-sahakari-bank-ltd-ifsc-code', 'the-varachha-co-op-bank-ltd-ifsc-code', 'the-vishweshwar-sahakari-bank-ltd-pune-ifsc-code', 'the-west-bengal-state-cooperative-bank-ltd-ifsc-code', 'the-zoroastrian-cooperative-bank-limited-ifsc-code', 'thrissur-district-co-operative-bank-ifsc-code', 'tjsb-sahakari-bank-ltd-ifsc-code', 'tumkur-grain-merchants-cooperative-bank-ltd-ifsc-code', 'ubs-ag-ifsc-code', 'uco-bank-ifsc-code', 'ujjivan-small-finance-bank-ifsc-code', 'union-bank-of-india-ifsc-code', 'united-bank-of-india-ifsc-code', 'united-overseas-bank-limited-ifsc-code', 'utkarsh-small-finance-bank-ifsc-code', 'vasai-janata-sahakari-bank-ltd-ifsc-code', 'vasai-vikas-sahakari-bank-ltd-ifsc-code', 'vijaya-bank-ifsc-code', 'westpac-banking-corporation-ifsc-code', 'woori-bank-ifsc-code', 'yes-bank-ltd-ifsc-code', 'zila-sahakri-bank-limited-ghaziabad-ifsc-code']
file = open("d:/states.csv","w")
for bank in banks:
    res = requests.get('https://banksifsccode.com/'+bank+'/')
    soup = bs4.BeautifulSoup(res.text,'lxml')
    links = soup.select('.bLists4 a')
    for link in links:
        states = link.get('href')
        writer = csv.writer(file)
        writer.writerow(states)
file.close()



# District will come #
states = ['andaman-and-nicobar']#'andhra-pradesh', 'goa', 'haryana', 'nagaland', 'arunachal-pradesh', 'daman-and-diu', 'meghalaya', 'uttar-pradesh', 'west-bengal', 'mizoram', 'pondicherry', 'jharkhand', 'bihar', 'sikkim', 'madhya-pradesh', 'uttaranchal', 'assam', 'uttarakhand', 'gujarat', 'maharashtra', 'tamil-nadu', 'kerala', 'new-delhi', 'dadra-and-nagar-haveli', 'chandigarh', 'delhi', 'orissa', 'lakshadweep', 'telangana', 'karnataka', 'tripura', 'punjab', 'odisha', 'rajasthan', 'chhattisgarh', 'himachal-pradesh', 'manipur', 'jammu-and-kashmir']
file = open("d:/districts10.csv","w")
for state in states:
    for bank in banks:
        res = requests.get('https://banksifsccode.com/'+bank+'/'+state+'/')
        soup = bs4.BeautifulSoup(res.text,'lxml')
        links = soup.select('.bLists4 a')
        for link in links:
            districts = link.get('href')
            writer = csv.writer(file)
            writer.writerow(districts)
file.close()

# Branches will come #
districts = ['nicobar', 'diglipur-north', 'garacharama','nicobar-islands', 'bidhannagar', 'south-andaman', 'port-blair', 'middle-andaman', 'mayabunder', 'chennai', 'andaman', 'port-blair-andaman-and-nicobar']
file = open("d:/andaman_nicobar_branches.csv","w")
for bank in banks:
    for state in states:
        for district in districts:
            res = requests.get('https://banksifsccode.com/'+bank+'/'+state+'/'+district+'/')
            soup = bs4.BeautifulSoup(res.text,'lxml')
            links = soup.select('.bLists4 a')
            for link in links:
                branches = link.get('href')
                writer = csv.writer(file)
                writer.writerow(branches)
file.close()

file = open("d:/andaman_nicobar_branches.csv","w")
a = open("d:/scrapbank/state wise district/andaman nicobar.txt","r")
b = a.readlines()
res = requests.get(b)
soup = bs4.BeautifulSoup(res.text,'lxml')
links = soup.select('.bLists4 a')
for link in links:
    branches = link.get('href')
    writer = csv.writer(file)
    writer.writerow(branches)
file.close()

    
