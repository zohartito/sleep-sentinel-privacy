# Sleep Sentinel Privacy Notice

Last updated: 2026-07-17

Sleep Sentinel is a wellness-only Garmin Connect IQ app for the Fenix 7S Pro. This notice explains how Sleep Sentinel (the "developer") handles information associated with Sleep Sentinel.

This notice is published at https://zohartito.github.io/sleep-sentinel-privacy/. If the notice moves, the developer will keep the prior location available as a redirect to the new location.

## Information The App Accesses And Stores

Sleep Sentinel can access oxygen-related history that the Fenix 7S Pro has already collected through Garmin's Pulse Ox feature. The **Recent Pulse Ox** view uses a rolling 10-hour window ending when the view is opened. It is Garmin-native comparator context, not a Garmin-defined sleep record.

Sleep Sentinel may store the following information in its app-local storage on the watch:

- app-owned session timestamps, oxygen-trend samples, associated heart-rate samples, and collection diagnostics;
- compact collection-quality and oxygen-trend summaries; and
- compact summaries derived from the Garmin-native Recent Pulse Ox comparator.

Sleep Sentinel does not create a user account, require sign-in, request location data, or collect your name or email address through the app.

## Local Storage And No-Network Behavior

Store v0.4 stores Sleep Sentinel data only in the app's own storage area on the watch. It does not send that data to the developer, a cloud service, an analytics service, an advertiser, or another third party. Local review works without a Sleep Sentinel account or server.

Store v0.4 does not request the Connect IQ `Communications` permission and contains no watch-side network upload path. A hosted upload feature is deferred to a later release and would require separate consent, security, physical verification, and privacy review before it could ship.

The **Export SSRAW** command prints a local text export to the Connect IQ Simulator or device console log. It does not upload or otherwise transmit the export. Anyone who chooses to copy or share an export outside the watch is responsible for where that copy is stored and who receives it.

## Garmin Data And Responsibility

Garmin's handling of information collected by Garmin services, Garmin Connect, and Garmin's own apps is governed by Garmin's privacy notices, not this notice.

Any information you choose to enter or store in Sleep Sentinel is submitted to Sleep Sentinel, not to Garmin, even though the current build keeps app data local on the watch and does not transmit it to the developer. Garmin has no responsibility or liability for information submitted to Sleep Sentinel or for the developer's handling of that information.

## Retention And Deletion On The Watch

Sleep Sentinel keeps a rolling local history of no more than 30 completed nights. When a new completed night would exceed that cap, the oldest saved night is removed automatically. For an app-owned night, its associated sample chunks are deleted when that night is removed. An in-progress session may be stored separately while the app records or recovers that session.

The current build does not provide an in-app control to delete an individual completed night or erase all history. To remove Sleep Sentinel and its app-local data, uninstall Sleep Sentinel from the watch using Garmin's app-management controls. Because the current build does not send watch data to the developer, the developer cannot view or remotely delete data held on the watch.

## Support Messages

If you email sleepsentinel@zohartito.com, the developer receives the email address you use, your message, and any attachments you include. This information is submitted to Sleep Sentinel, not Garmin. It is used only to respond to the request, investigate the reported issue, and keep reasonable support or security records. It is not sold or used for advertising or analytics.

**Do not email health data, oxygen readings, sleep records, SSRAW exports, or other sensitive personal information.** The developer does not need that information to handle an ordinary support or privacy request.

Support messages are kept only as long as reasonably needed for those purposes and are then deleted. You may request earlier deletion of a support message by emailing sleepsentinel@zohartito.com from the same address and identifying the message. A minimal record may be retained when reasonably necessary to document a resolved security or privacy request or to meet an applicable legal obligation.

## Sharing

The current build does not sell, rent, or share Sleep Sentinel data with advertisers, analytics services, data brokers, or other third parties. A future version will not enable a network upload or materially change how data is collected, used, stored, or disclosed without first updating this notice at https://zohartito.github.io/sleep-sentinel-privacy/.

## Contact

Developer: Sleep Sentinel

Privacy and support email: sleepsentinel@zohartito.com

Policy URL: https://zohartito.github.io/sleep-sentinel-privacy/

Sleep Sentinel provides wellness oxygen-trend information only. Trend review only. This notice describes data handling; it is not health guidance.
