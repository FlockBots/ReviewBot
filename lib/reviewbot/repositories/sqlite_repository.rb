require 'sqlite3'

module ReviewBot
  module Repositories
    class Sqlite < Repository
      def initialize(limit, database)
        @db = SQLite3::Database.new database
        super(limit)
      end

      def columns
        %w(whisky
            region
            redditor
            url
            subreddit
            rating
            published_at).join(', ')
      end

      def limit
        "LIMIT #{@limit}"
      end

      def order
        "ORDER BY published_at DESC"
      end

      def recent_reviews(username)
        query = <<-SQL.strip
          SELECT #{columns} FROM database_reviews WHERE redditor = ? #{order} #{limit}
        SQL
        results = @db.execute(query, [username])
        results.map { |result| ReviewBot::Review.new(*result) }
      end

      def subreddit_reviews(username, subreddit)
        query = <<-SQL.strip
          SELECT #{columns} FROM database_reviews WHERE
          lower(redditor) = ? AND lower(subreddit) = ? #{order} #{limit}
        SQL
        results = @db.execute(query, [username.downcase, subreddit.downcase])
        results.map { |result| ReviewBot::Review.new(*result) }
      end

      def whisky_reviews(username, whisky)
        whisky = "%#{whisky}%".downcase
        query = <<-SQL.strip
          SELECT #{columns} FROM database_reviews WHERE
          lower(redditor) = ? AND lower(whisky) LIKE ? #{order} #{limit}
        SQL
        results = @db.execute(query, [username.downcase, whisky])
        results.map { |result| ReviewBot::Review.new(*result) }
      end
    end
  end
end
