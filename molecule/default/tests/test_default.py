def test_is_nginx_installed(host):
    assert host.package("nginx").is_installed


def test_service_nginx_running(host):
    assert host.service("nginx").is_running is True
