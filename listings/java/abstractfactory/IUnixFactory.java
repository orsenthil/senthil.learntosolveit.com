public interface IUnixFactory {
    IBootLoader installBootLoader();
    IKernel installKernel();
    IShell installShell();
    IDisplayManager  installDisplayManager();
    IWindowManager installWindowManager();
    IBaseApplications installApps();
}
