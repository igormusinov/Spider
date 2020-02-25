# Spider

## WebScraping for the Leadership research project.

## Install

LoL, only python

## VK-API scraping

### Create your own VK App

1. Create your VK application here `https://vk.com/apps?act=manage` . 
You need a Standalone app. Get your `APP_ID` in the app's settings.

2. You have to create `execute stored procedures` in your App (https://vk.com/apps?act=manage).
Find in the app's settings `Stored procedures`. Create new procedure `execute.singleLeader` :

```Javascript
var user = API.users.get({"user_ids": [Args.user], "fields": ["photo_id", "verified", "sex", "bdate", "city", "country", "home_town", "has_photo", "photo_50", "photo_100", "photo_200_orig", "photo_200", "photo_400_orig", "photo_max", "photo_max_orig", "online", "domain", "has_mobile", "contacts", "site", "education", "universities", "schools", "status", "last_seen", "followers_count", "common_count", "occupation", "nickname", "relatives", "relation", "personal", "connections", "exports", "activities", "interests", "music", "movies", "tv", "books", "games", "about", "quotes", "can_post", "can_see_all_posts", "can_see_audio", "can_write_private_message", "can_send_friend_request", "is_favorite", "is_hidden_from_feed", "timezone", "screen_name", "maiden_name", "crop_photo", "is_friend", "friend_status", "career", "military", "blacklisted", "blacklisted_by_me", "can_be_invited_group"]});

var groups = API.groups.get({"user_id": Args.user, "extended": 1});

var wall = API.wall.get({"owner_id": Args.user, "extended": 1});
  
return [user, groups, wall];
```

### Use existing VK App

3. Get the `ACCESS_TOKEN` for your app. 
Open in your browser (specify `<APP_ID>` from 1 step in the request)
 `https://oauth.vk.com/authorize?client_id=<APP_ID>&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.103&state=123456`
 . You will be redirected to another page, in the browser's search string you will find you `ACCESS_TOKEN`. 


4. Set this `ACCESS_TOKEN` inside of the notebook 

`!!! Don't commit the token to the repo. You can lose an access to your account !!!`

5. Get `users.csv` file

6. Launch notebook `vk_api_scrap.ipynb`



### Usefull links

https://vk.com/dev/authcode_flow_user

https://vk.com/dev/methods

https://vk.com/dev/execute

https://vk.com/dev/users

https://vk.com/dev/groups

https://vk.com/dev/wall

https://vk.com/dev/likes 

STREAMING API? https://vk.com/dev/streaming_api_docs

## No-API scraping [deprecated]

scrap.ipynb 
