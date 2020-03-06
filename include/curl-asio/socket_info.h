/**
	curl-asio: wrapper for integrating libcurl with boost.asio applications
	Copyright (c) 2013 Oliver Kuckertz <oliver.kuckertz@mologie.de>
	See COPYING for license information.
*/

#pragma once

#include <boost/asio.hpp>
#include <memory>

namespace curl
{
	typedef boost::asio::ip::tcp::socket socket_type;

	class easy;

	struct socket_info : public std::enable_shared_from_this<socket_info>
	{
		socket_info(easy* _handle, std::unique_ptr<socket_type> _socket):
			handle(_handle),
			socket(std::move(_socket)),
			pending_read_op(false),
			pending_write_op(false),
			monitor_read(false),
			monitor_write(false)
		{
		}
		
		easy* handle;
		std::unique_ptr<socket_type> socket;
		bool pending_read_op;
		bool pending_write_op;
		bool monitor_read;
		bool monitor_write;
	};
}
