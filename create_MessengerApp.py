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

