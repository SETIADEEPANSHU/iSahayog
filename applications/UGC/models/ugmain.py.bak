# -*- coding: utf-8 -*-
temp=local_import('states')
ans=temp.getStates()
dist=temp.getDist('Bihar')
db.define_table('Problems',
                Field('p_category','string',label='Problem category',writable=False,readable=True,default=''),
                Field('p_id','integer',writable=False,label='Problem Id',readable=False),
                Field('p_userid','string',required=True,requires=IS_EMAIL(),label='Email Id'),
                Field('p_loc','string',required=True,requires=IS_NOT_EMPTY('Enter Location'),label='Location'),
                Field('p_text','text',required=True,requires=IS_NOT_EMPTY('Enter Problem Description'),label='Problem Description'),
                Field('p_status','string',requires=IS_IN_SET(['Pending','In Progress','Completed','Approved','Verified']),label='Status'),
                Field('problem_source','string')
                )
db.define_table('Mappings',
                Field('p_id','integer'),
                Field('c_id','integer'),
                Field('p_category','text')
                )
db.define_table('Colleges',
                Field('c_id','integer',required=True,requires=IS_NOT_EMPTY('Fill College ID')),
                Field('c_name','text',required=True,requires=IS_NOT_EMPTY('Fill College Name')),
                Field('c_email','string',required=True,requires=IS_EMAIL()),
                Field('c_loc','text',required=True,requires=IS_NOT_EMPTY('Fill College Location'))
                )
db.define_table('Solutions',
                Field('p_id','integer',default=' ',required=True,requires=IS_NOT_EMPTY('Enter or Select Problem ID'),label='Problem ID'),
                Field('contact','string',required=True,requires=IS_EMAIL(),label='Contact Email ID'),
                Field('c_id','string',label='College ID'),
                Field('solution','text',label='Solution Description'),
                Field('colo','string'),
                Field('myfile','upload'),
                Field('status','string')
                  )
#db.Solutions.myfile.requires=IS_UPLOAD_FILENAME(extension='pdf')
db.define_table('Logins',
                Field('c_id','integer',required=True,requires=IS_NOT_EMPTY('Enter your College ID')),
                Field('c_pass','password',required=True,requires=IS_NOT_EMPTY('Enter your password'))
                )
db.define_table('Locate',
                 Field('states',requires=IS_IN_SET(ans)))
#Scheduling Testing chal rahi hai Niche. Iske bad wala comment ke bad apna code likhe
db.define_table('Testing',
                Field('Texts','text'),
                Field('u_name','string'),
                Field('u_loc','string'),
                Field('t_loc','string'),
                Field('isRetweet','string')
                )
###### Yaha ke bad apna code likhe.
db.define_table('Col',
                Field('ss_id','integer'),
                Field('ch_id','string'),
                Field('json_data','string')
                )
db.define_table('Slck',
                Field('user_id','string'),
                Field('slack_pass','string')
               )
db.define_table('Rankings',
                Field('loc','string'),
                Field('category','string'),
                Field('r_ank','integer'),
                Field('twitter_cnt','integer'),
                Field('news_cnt','integer'),
                Field('portal_cnt','integer'),
                Field('grieavance_portal','integer'),
                Field('F_Agency','string')
                )
db.define_table('Funded',
          Field('college','string'),
          Field('Funding_Agency','string'),
          Field('p_id','integer')
          )
