public class LinuxFactory implements IUnixFactory {
    @Override
    public IBootLoader installBootLoader() {
        return new LinuxBootLoader();
    }

    @Override
    public IKernel installKernel() {
        return new Linux();
    }

    @Override
    public IShell installShell() {
        return new Bash();
    }

    @Override
    public IDisplayManager installDisplayManager() {
        return new X11();
    }

    @Override
    public IWindowManager installWindowManager() {
        return new Gnome();
    }

    @Override
    public IBaseApplications installApps() {
        return new GNUApplications();
    }
}
