#lembrar de executar 
#$ mysql.server start

import processor.sorting
import processor.tweet_search
from view import *
import view.main
import db.lp



if __name__ == '__main__':
    view.main.Login_GUI().run()

