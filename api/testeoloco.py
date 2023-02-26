from collections import OrderedDict
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# array_map
# response
#----------------------------

def showByName(Request request) :

    name = request.route('name');
    include = request.include.lower();
    arrayInclude = include.split(",");
    #$includes = array_map('strtolower', $arrayInclude);
    items_per_page = request.items_per_page;
    history = OrderedDict([(0,"history")]);
    crests = OrderedDict([(0,"crests")]);
    products = OrderedDict([(0,"products")]);
    historyandcrests = OrderedDict([(0,"history"),(1,"crests")]);
    crestsandproducts = OrderedDict([(0,"crests"),(1,"products")]);
    historyandproducts = OrderedDict([(0,"history"),(1,"products")]);
    all = OrderedDict([(0,"history"),(1,"crests"),(2,"products")]);
    lowercaseallowed = array_map('strtolower', all);


        if (this.in_array_all(arrayInclude, lowercaseallowed) == True and len(arrayInclude) <= 3) :
            if (True == this.sameElements(arrayInclude, history) == 1) :
                names = Family.select('name_id', 'name', 'country', 'clan', 'info').where('name', 'LIKE', str('%' + str(name)) + '%').paginate(items_per_page);
                return response().json(OrderedDict([('status',True),('names',names)]));
            elif (True == this.sameElements(arrayInclude, crests) == 1) :
                names = Family.select('name_id', 'name', 'country', 'clan').where('name', 'LIKE', str('%' + str(name)) + '%').with('crests:crest_id,crest_url,caption,clan,name_id').paginate(items_per_page);
                return response().json(OrderedDict([('status',True),('names',names)]));
            elif (True == this.sameElements(arrayInclude, products) == 1) :
                names = Family.select('name_id', 'name', 'country', 'clan').where('name', 'LIKE', str('%' + str(name)) + '%').with('images:img_id,image_url,image_info,type,name_id').paginate(items_per_page);
                return response().json(OrderedDict([('status',True),('names',names)]));
            elif (True == this.sameElements(arrayInclude, historyandcrests) == 1) :
                names = Family.select('name_id', 'name', 'country', 'clan', 'info').where('name', 'LIKE', str('%' + str(name)) + '%').with('crests:crest_id,crest_url,caption,clan,name_id').paginate(items_per_page);
                return response().json(OrderedDict([('status',True),('names',names)]));
            elif (True == this.sameElements(arrayInclude, crestsandproducts) == 1) :
                names = Family.select('name_id', 'name', 'country', 'clan', 'info').where('name', 'LIKE', str('%' + str(name)) + '%').with('crests:crest_id,crest_url,caption,clan,name_id', 'images:img_id,image_url,image_info,type,name_id').paginate(items_per_page);
                return response().json(OrderedDict([('status',True),('names',names)]));
            elif (True == this.sameElements(arrayInclude, historyandproducts) == 1) :
                names = Family.select('name_id', 'name', 'country', 'clan', 'info').where('name', 'LIKE', str('%' + str(name)) + '%').with('images:img_id,image_url,image_info,type,name_id').paginate(items_per_page);
                return response().json(OrderedDict([('status',True),('names',names)]));
            elif (True == this.sameElements(arrayInclude, all) == 1) :
                names = Family.select('name_id', 'name', 'country', 'clan', 'info').where('name', 'LIKE', str('%' + str(name)) + '%').with('crests:crest_id,crest_url,caption,clan,name_id', 'images:img_id,image_url,image_info,type,name_id').paginate(items_per_page);
                return response().json(OrderedDict([('status',True),('names',names)]));
        else : 
            print("Pusiste cualquier cosa",end="");