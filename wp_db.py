from gluon.dal import *
from gluon.validators import IS_IN_SET

WP_USER = 'inspect'
WP_PASS = 'inspect'
WP_HOST = 'localhost'
WP_DB = 'inspect'
WP_PREFIX = 'wp_'

db = DAL('mysql://inspect:inspect@localhost/inspect')

db.define_table('users',
    Field('ID','id'),
    Field('user_login','string'),
    Field('user_pass','string'),
    Field('user_nicename','string'),
    Field('user_email','string'),
    Field('user_url','string'),
    Field('user_registered','datetime'),
    Field('user_activation_key','string'),
    Field('user_status','integer'),
    Field('display_name','string'),
    rname=WP_PREFIX + 'users',
    migrate=False)

db.define_table('posts',
    Field('ID','id'),
    Field('post_author','refrence user'),
    Field('post_date','datetime'),
    Field('post_date_gmt','datetime'),
    Field('post_content','text'),
    Field('post_title','text'),
    Field('post_excerpt','text'),
    Field('post_status','string'),
    Field('comment_status','string'),
    Field('ping_status','string'),
    Field('post_password','string'),
    Field('post_name','string'),
    Field('to_ping','text'),
    Field('pinged','text'),
    Field('post_modified','datetime'),
    Field('post_modified_gmt','datetime'),
    Field('post_content_filtered','text'),
    Field('post_parent','integer'),
    Field('guid','string'),
    Field('menu_order','integer'),
    Field('post_type','string'),
    Field('post_mime_type','string'),
    Field('comment_count','integer'),
    rname=WP_PREFIX + 'posts',
    migrate=False)

db.define_table('comments',
    Field('comment_ID','id'),
    Field('comment_post_ID', db.posts),
    Field('comment_author','text'),
    Field('comment_author_email','string'),
    Field('comment_author_url','string'),
    Field('comment_author_IP','string'),
    Field('comment_date','datetime'),
    Field('comment_date_gmt','datetime'),
    Field('comment_content','text'),
    Field('comment_karma','integer'),
    Field('comment_approved','string'),
    Field('comment_agent','string'),
    Field('comment_type','string'),
    Field('comment_parent','integer'),
    Field('user_id','integer', 
          requires=IS_IN_SET([(0, 'Unregistered')] + 
                             [ (user.ID, user.user_nicename) for user in db(db.users).select()])), # NOTE: 0 means no userid for this comment. That's why this table doesn't refrence the user table
    rname=WP_PREFIX + 'comments',
    migrate=False)

db.define_table('commentmeta',
    Field('meta_id','id'),
    Field('comment_id','integer'),
    Field('meta_key','string'),
    Field('meta_value','text'),
    rname=WP_PREFIX + 'commentmeta',
    migrate=False)

db.define_table('links',
    Field('link_id','id'),
    Field('link_url','string'),
    Field('link_name','string'),
    Field('link_image','string'),
    Field('link_target','string'),
    Field('link_description','string'),
    Field('link_visible','string'),
    Field('link_owner','integer'),
    Field('link_rating','integer'),
    Field('link_updated','datetime'),
    Field('link_rel','string'),
    Field('link_notes','text'),
    Field('link_rss','string'),
    rname=WP_PREFIX + 'links',
    migrate=False)

db.define_table('options',
    Field('option_id','id'),
    Field('option_name','string'),
    Field('option_value','text'),
    Field('autoload','string'),
    rname=WP_PREFIX + 'options',
    migrate=False)

db.define_table('postmeta',
    Field('meta_id','id'),
    Field('post_id',db.posts),
    Field('meta_key','string'),
    Field('meta_value','text'),
    rname=WP_PREFIX + 'postmeta',
    migrate=False)

db.define_table('terms',
    Field('term_id','id'),
    Field('name','string'),
    Field('slug','string'),
    Field('term_group','integer'),
    rname=WP_PREFIX + 'terms',
    migrate=False)

db.define_table('term_relationships',
    Field('object_id','id'),
    Field('term_taxonomy_id','integer'),
    Field('term_order','integer'),
    rname=WP_PREFIX + 'term_relationships',
    migrate=False)

db.define_table('term_taxonomy',
    Field('term_taxonomy_id','id'),
    Field('term_id', db.terms),
    Field('taxonomy','string'),
    Field('description','text'),
    Field('parent','integer'),
    Field('count','integer'),
    rname=WP_PREFIX + 'term_taxonomy',
    migrate=False)

db.define_table('usermeta',
    Field('umeta_id','id'),
    Field('user_id', db.users),
    Field('meta_key','string'),
    Field('meta_value','text'),
    rname=WP_PREFIX + 'usermeta',
    migrate=False)
