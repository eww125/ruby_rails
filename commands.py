sudo gem install rails
rails new MySite
cd MySite
bundle install
rails server
#spring stop

rails generate controller Pages
#app/controllers/pages_controller.rb
class PagesController < ApplicationController
  def home
  end
end

#config/routes.rb
Rails.application.routes.draw do
  get 'welcome' => 'pages#home'
end

#app/views/pages/home.html.erb (create)
<div class="main">
  <div class="container">
    <h1>Hello my name is Pewt</h1>
    <p>I make Rails apps.</p>
  </div>
</div>

#app/assets/stylesheets/pages.css.scss
https://raw.githubusercontent.com/eww125/ruby_rails/master/pages.css.scss
