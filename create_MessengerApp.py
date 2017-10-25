rails new MessengerApp
cd MessengerApp
bundle install

rails generate model Message
#db/migrate/20171025182746_create_messages.rb
class CreateMessages < ActiveRecord::Migration[5.1]
  def change
    create_table :messages do |t|
      t.text :content
      t.timestamps
    end
  end
end

rake db:migrate
rake db:seed

rails generate controller Messages
#app/controllers/messages_controller.rb)
class MessagesController < ApplicationController
  def index 
    @messages = Message.all 
  end
end

#app/views/messages/index.html.erb
<div class="header">
  <div class="container">
    <img src="http://s3.amazonaws.com/codecademy-content/courses/learn-rails/img/logo-1m.svg">
    <h1>Messenger</h1>
  </div>
</div>

<div class="messages">
  <div class="container">

    <!-- Your code here -->
<% @messages.each do |message| %>
<div class="message">
  <p class="content"><%= message.content %></p>
  <p class="time"><%= message.created_at %></p>
</div>
<% end %>

<%= link_to 'New Message', "messages/new" %>

  </div>
</div>

