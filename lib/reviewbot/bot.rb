require 'redd'

module ReviewBot
  # include Commands

  class Bot
    include Commands

    def initialize(session, review_repository)
      @session = session
      @repository = review_repository

      @limit = 10 # todo: move to config?
    end

    def username
      @session.me.name
    end

    def inbox
      @session.my_messages(mark: false)
    end

    def watch_reddit
      # todo: create endless stream?
      inbox.each { |message| analyze message }
    end

    def analyze(message)
      @current_message = message
      @repository.user = message.author.name

      commands = [recent_command, subreddit_command, whisky_command]
      commands.each do |command|
        results = command.match(message.body) # [<CommandResult>]
        results.map {|result| build_reply(result)}
      end

      reply
    end

    def build_reply(result)
      return if result.return_value.nil?
      @reply_body = "/u/#{@current_message.author.name}'s latest reviews"
      @reply_body += " (#{result.parameters.first})" if !result.parameters.empty?
      @reply_body += "\n\n"
      result.return_value.each do |review|
        @reply_body += "* [#{review.whisky}](#{review.url})\n"
      end
      @reply_body += "\n"
    end

    def reply
      puts @reply_body
    end

    private

    def recent_command
      prefix = "/u/#{username} latest"
      regex = /#{Regexp.quote(prefix)}/i
      Command.new(regex) do
        @repository.recent_reviews
      end
    end

    def subreddit_command
      prefix = "/u/#{username} /r/"

      # command taken from reddit source: reddit/reddit: r2/models/subreddit.py
      subreddit = /[A-Za-z0-9][A-Za-z0-9_]{2,20}/
      regex = /#{Regexp.quote(prefix)}(#{subreddit})($|[^A-Za-z0-9_])/i
      ParameterizedCommand.new(regex, [0]) do |name|
        @repository.subreddit_reviews(name)
      end
    end

    def whisky_command
      prefix = "/u/#{username}"
      regex = /#{Regexp.quote(prefix)} (["'])((?:\\\1|.)*?)\1/i
      ParameterizedCommand.new(regex, [1]) do |whisky|
        whisky.delete!('\\')
        @repository.whisky_reviews(whisky)
      end
    end
  end
end
